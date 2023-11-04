# Import Libraries
from config.config import BINARY_RELEVANCE_ENCODED_VALUES, COLUMN_NEW_ORDER, COLUMN_RENAME_DICT, ONE_HOT_ENCODED_VALUES, Requirements
from fastapi import FastAPI
from ml_from_scratch.MatrixFactorization import AlternatingLeastSquaresFactorization
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import json
import numpy as np
import pandas as pd
import pickle

# Initialization
df_original = pd.read_pickle('/app/data/processed/df_preprocessed.pkl')
df_encoded = pd.read_pickle('/app/data/processed/df_processed_encoded.pkl')
with open('/app/models/alsf_model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('/app/models/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
app = FastAPI()


def rename_and_sort_columns(df):
    df = df.rename(columns=COLUMN_RENAME_DICT)
    df = df[COLUMN_NEW_ORDER]
    return df


def feature_scaler(df):
    df[["YearsCode"]] = scaler.transform(df[["YearsCode"]])
    return df


def binary_relevance_encoding(df, columns_possibilities=BINARY_RELEVANCE_ENCODED_VALUES):
    new_cols = []
    for column, binary_relevance_encoded_values in columns_possibilities.items():
        df[column] = df[column].apply(
            lambda x: x.split(";") if pd.notna(x) else [])
        df_temporary = pd.DataFrame()
        for value in binary_relevance_encoded_values:
            new_column_name = f"{column}_{value}"
            df_temporary[new_column_name] = df[column].apply(
                lambda x: 1 if value in x else 0)
        new_cols.append(df_temporary)
        df.drop(column, axis=1, inplace=True)
    df = pd.concat([df] + new_cols, axis=1)
    return df


def one_hot_encoding(df, columns_possibilities=ONE_HOT_ENCODED_VALUES):
    for column, one_hot_encoded_values in columns_possibilities.items():
        dummies = pd.get_dummies(df[column], prefix=column)
        new_column_name = {f"{column}_{value}": [
            0] * len(df) for value in one_hot_encoded_values}
        new_cols = pd.DataFrame(new_column_name)
        new_cols.update(dummies)
        df = df.drop(column, axis=1)
        df = pd.concat([df, new_cols], axis=1)
    return df


def predict(df):
    prediction = model.predict(df)
    return prediction


def find_most_similar_candidates(predicted_values, df_encoded=df_encoded, df_original=df_original, top_n=10):
    similarities = cosine_similarity([predicted_values], df_encoded.values)
    sorted_indices = np.argsort(similarities[0])[::-1]
    top_candidates_indices = sorted_indices[:top_n]
    top_candidates_with_identifiers = df_original.iloc[top_candidates_indices]
    return top_candidates_with_identifiers


@app.post('/recommend')
def recommend_candidate(requirements: Requirements):
    df = pd.DataFrame([requirements.dict()])
    df = rename_and_sort_columns(df)
    df = feature_scaler(df)
    df = binary_relevance_encoding(df)
    df = one_hot_encoding(df)
    prediction = predict(df).flatten()
    similar_candidates = find_most_similar_candidates(prediction)
    candidates = similar_candidates.to_dict(orient='records')
    return {"recommended_candidates": candidates}
