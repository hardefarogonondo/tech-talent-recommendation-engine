# Import Libraries
import json
import pandas as pd
import requests
import streamlit as st

# Initialization
API_URL = 'http://backend:8000/recommend'
with open('config/config.json', 'r') as config_file:
    input_options = json.load(config_file)


def select_multiple_options(title, options, num_cols=5):
    st.subheader(title)
    cols = st.columns(num_cols)
    selected_options = []
    for i, option in enumerate(options):
        with cols[i % num_cols]:
            if st.checkbox(option):
                selected_options.append(option)
    return selected_options


def main():
    # Main UI
    st.title("Tech Talent Recommendation Engine")

    # Candidate's Personal Information Inputs
    st.header("Candidate's Personal Information")
    age_ranges = st.selectbox("Age Range", input_options["age_ranges"])
    work_arrangements = st.selectbox(
        "Work Arrangement", input_options["work_arrangements"])
    education_levels = st.selectbox(
        "Education Level", input_options["education_levels"])
    roles = st.selectbox("Role", input_options["roles"])
    years_of_experience = st.number_input("Years of Experience", min_value=0)

    # Candidate's Technical Skills Inputs
    st.header("Candidate's Technical Skills")
    programming_languages = select_multiple_options(
        "Programming Languages", input_options["programming_languages"])
    databases = select_multiple_options(
        "Databases", input_options["databases"])
    cloud_platforms = select_multiple_options(
        "Cloud Platforms", input_options["cloud_platforms"])
    web_frameworks = select_multiple_options(
        "Web Frameworks", input_options["web_frameworks"])
    other_frameworks = select_multiple_options(
        "Other Frameworks", input_options["other_frameworks"])
    developer_tools = select_multiple_options(
        "Developer Tools", input_options["developer_tools"])
    development_environments = select_multiple_options(
        "Development Environments", input_options["development_environments"])
    operating_systems = select_multiple_options(
        "Operating Systems", input_options["operating_systems"])
    collaboration_tools = select_multiple_options(
        "Collaboration Tools", input_options["collaboration_tools"])
    communication_tools = select_multiple_options(
        "Communication Tools", input_options["communication_tools"])

    # Recommend Button
    if st.button("Recommend"):
        data = {
            "age_range": age_ranges,
            "work_arrangement": work_arrangements,
            "education_level": education_levels,
            "role": roles,
            "years_of_experience": years_of_experience,
            "programming_languages": ";".join(programming_languages),
            "databases": ";".join(databases),
            "cloud_platforms": ";".join(cloud_platforms),
            "web_frameworks": ";".join(web_frameworks),
            "other_frameworks": ";".join(other_frameworks),
            "developer_tools": ";".join(developer_tools),
            "development_environments": ";".join(development_environments),
            "operating_systems": ";".join(operating_systems),
            "collaboration_tools": ";".join(collaboration_tools),
            "communication_tools": ";".join(communication_tools)
        }
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            st.success("Candidates successfully recommended.")
            recommendations = response.json().get("recommended_candidates", [])
            recommendations_df = pd.DataFrame(recommendations)
            st.dataframe(recommendations_df)
        else:
            st.error(
                f"Failed to get recommendations. Status code: {response.status_code} Response: {response.text}")


if __name__ == "__main__":
    main()
