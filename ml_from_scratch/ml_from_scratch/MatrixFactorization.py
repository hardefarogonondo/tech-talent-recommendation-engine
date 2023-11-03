import numpy as np
import pandas as pd


class AlternatingLeastSquaresFactorization:
    def __init__(self, iterations=10, num_factors=10, regularization=0.1):
        self.iterations = iterations
        self.num_factors = num_factors
        self.regularization = regularization
        self.talents_factors = None
        self.skills_factors = None

    def factorization(self):
        return np.dot(self.talents_factors, self.skills_factors.T)

    def calculate_mse(self, X):
        factorized_matrix = self.factorization()
        mask = np.nonzero(X)
        mse = np.mean((X[mask] - factorized_matrix[mask]) ** 2)
        return mse

    def calculate_mae(self, X):
        factorized_matrix = self.factorization()
        mask = np.nonzero(X)
        mae = np.mean(np.abs(X[mask] - factorized_matrix[mask]))
        return mae

    def _als_step(self, status, solve_vectors, fixed_vectors):
        YTY = fixed_vectors.T.dot(fixed_vectors)
        lambdaI = np.eye(YTY.shape[0]) * self.regularization
        for u in range(solve_vectors.shape[0]):
            if isinstance(status, pd.DataFrame):
                user_status = status.iloc[u].values
            else:
                user_status = status[u]
            solve_vectors[u] = np.linalg.solve(
                YTY + lambdaI, user_status.dot(fixed_vectors))
        return solve_vectors

    def fit(self, tech_talents_matrix):
        if isinstance(tech_talents_matrix, pd.DataFrame):
            tech_talents_matrix = tech_talents_matrix.to_numpy()
        num_talents, num_skills = tech_talents_matrix.shape
        self.talents_factors = np.random.normal(
            scale=1./self.num_factors, size=(num_talents, self.num_factors))
        self.skills_factors = np.random.normal(
            scale=1./self.num_factors, size=(num_skills, self.num_factors))
        for iteration in range(self.iterations):
            self.talents_factors = self._als_step(
                tech_talents_matrix, self.talents_factors, self.skills_factors)
            self.skills_factors = self._als_step(
                tech_talents_matrix.T, self.skills_factors, self.talents_factors)
            mse = self.calculate_mse(tech_talents_matrix)
            mae = self.calculate_mae(tech_talents_matrix)
            print(f"Iteration: {iteration + 1}, MSE: {mse}, MAE: {mae}")
        return self

    def predict(self, df):
        if isinstance(df, pd.DataFrame):
            df_array = df.to_numpy()
        else:
            df_array = df
        num_talents, num_skills = df_array.shape
        predictions = np.zeros((num_talents, num_skills))
        for i in range(num_talents):
            for j in range(num_skills):
                predictions[i, j] = np.dot(
                    self.talents_factors[i, :], self.skills_factors[j, :].T)
        return predictions


class GradientDescentFactorization:
    def __init__(self, lambda_reg=0.1, learning_rate=0.01, num_epochs=100, num_factors=10):
        self.lambda_reg = lambda_reg
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.num_factors = num_factors

    def factorization(self):
        return np.dot(self.talents_factors, self.skills_factors.T)

    def calculate_mse(self, X):
        factorized_matrix = self.factorization()
        mask = np.nonzero(X)
        mse = np.mean((X[mask] - factorized_matrix[mask]) ** 2)
        return mse

    def calculate_mae(self, X):
        factorized_matrix = self.factorization()
        mask = np.nonzero(X)
        mae = np.mean(np.abs(X[mask] - factorized_matrix[mask]))
        return mae

    def fit(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()
        num_talents, num_skills = X.shape
        self.talents_factors = np.random.normal(
            scale=1./self.num_factors, size=(num_talents, self.num_factors))
        self.skills_factors = np.random.normal(
            scale=1./self.num_factors, size=(num_skills, self.num_factors))
        for epoch in range(self.num_epochs):
            for i in range(num_talents):
                for j in range(num_skills):
                    if X[i, j] > 0:
                        err = X[i, j] - np.dot(self.talents_factors[i, :],
                                               self.skills_factors[j, :].T)
                        self.talents_factors[i, :] += self.learning_rate * (
                            err * self.skills_factors[j, :] - self.lambda_reg * self.talents_factors[i, :])
                        self.skills_factors[j, :] += self.learning_rate * (
                            err * self.talents_factors[i, :] - self.lambda_reg * self.skills_factors[j, :])
            mse = self.calculate_mse(X)
            mae = self.calculate_mae(X)
            print(f"Epoch: {epoch+1}, MSE: {mse}, MAE: {mae}")
        return self

    def predict(self, df):
        if isinstance(df, pd.DataFrame):
            df_array = df.to_numpy()
        else:
            df_array = df
        num_talents, num_skills = df_array.shape
        if num_talents > self.talents_factors.shape[0] or num_skills > self.skills_factors.shape[0]:
            raise ValueError(
                "DataFrame contains more data than the model was trained on.")
        return np.dot(self.talents_factors[:num_talents, :], self.skills_factors[:num_skills, :].T)
