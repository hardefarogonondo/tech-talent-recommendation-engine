import json
import streamlit as st

with open("config/config.json", "r") as config_file:
    config = json.load(config_file)

# Title of the web app
st.title("Tech Talent Recommendation Engine")

# 1. Age of the Candidate
ages = config["ages"]
age = st.selectbox(
    "Age of The Candidate Wanted",
    ages
)

# 2. Work Preferences
work_preferences = config["work_preferences"]
work_pref = st.selectbox(
    "Work Preferences",
    work_preferences
)

# 3. Education Level
education_levels = config["education_levels"]
education = st.selectbox(
    "Education Level",
    education_levels
)

# 4. Developer Type
developer_types = config["developer_types"]
dev_type = st.selectbox(
    "Developer Type",
    developer_types
)

num_cols = 5

# 5. Programming Language
st.subheader("Programming Languages")
programming_languages = config["programming_languages"]
cols = st.columns(num_cols)
selected_programming_languages = []
for i, lang in enumerate(programming_languages):
    with cols[i % num_cols]:
        if st.checkbox(lang, key=f'prog_lang_{lang}'):
            selected_programming_languages.append(lang)

# 6. Database
st.subheader("Databases")
databases = config["databases"]
cols = st.columns(num_cols)
selected_databases = []
for i, db in enumerate(databases):
    with cols[i % num_cols]:
        if st.checkbox(db, key=f'db_{db}'):
            selected_databases.append(db)

# 7. Cloud Platform
st.subheader("Cloud Platforms")
cloud_platforms = config["cloud_platforms"]
cols = st.columns(num_cols)
selected_cloud_platforms = []
for i, platform in enumerate(cloud_platforms):
    with cols[i % num_cols]:
        if st.checkbox(platform, key=f'cloud_{platform}'):
            selected_cloud_platforms.append(platform)

# 8. Web Framework
st.subheader("Web Frameworks")
web_frameworks = config["web_frameworks"]
cols = st.columns(num_cols)
selected_web_frameworks = []
for i, framework in enumerate(web_frameworks):
    with cols[i % num_cols]:
        if st.checkbox(framework, key=f'web_fw_{framework}'):
            selected_web_frameworks.append(framework)

# 9. Other Framework
st.subheader("Other Frameworks")
other_frameworks = config["other_frameworks"]
cols = st.columns(num_cols)
selected_other_frameworks = []
for i, framework in enumerate(other_frameworks):
    with cols[i % num_cols]:
        if st.checkbox(framework, key=f'other_fw_{framework}'):
            selected_other_frameworks.append(framework)

# 10. Developer Tools
st.subheader("Developer Tools")
developer_tools = config["developer_tools"]
cols = st.columns(num_cols)
selected_developer_tools = []
for i, tool in enumerate(developer_tools):
    with cols[i % num_cols]:
        if st.checkbox(tool, key=f'dev_tool_{tool}'):
            selected_developer_tools.append(tool)

# 11. Development Environment
st.subheader("Development Environments")
development_environments = config["development_environments"]
cols = st.columns(num_cols)
selected_development_environments = []
for i, env in enumerate(development_environments):
    with cols[i % num_cols]:
        if st.checkbox(env, key=f'dev_env_{env}'):
            selected_development_environments.append(env)

# 12. Operating System
st.subheader("Operating Systems")
operating_systems = config["operating_systems"]
cols = st.columns(num_cols)
selected_operating_systems = []
for i, operating_system in enumerate(operating_systems):
    with cols[i % num_cols]:
        if st.checkbox(operating_system, key=f'operating_system_{operating_system}'):
            selected_operating_systems.append(operating_system)

# 13. Collaborative Work Management Tools
st.subheader("Collaborative Work Management Tools")
collaboration_tools = config["collaboration_tools"]
cols = st.columns(num_cols)
selected_collaboration_tools = []
for i, collaboration_tools in enumerate(collaboration_tools):
    with cols[i % num_cols]:
        if st.checkbox(collaboration_tools, key=f'collaboration_tools_{collaboration_tools}'):
            selected_collaboration_tools.append(collaboration_tools)

# 14. Communication Tools
st.subheader("Communication Tools")
communication_tools = config["communication_tools"]
cols = st.columns(num_cols)
selected_communication_tools = []
for i, communication_tools in enumerate(communication_tools):
    with cols[i % num_cols]:
        if st.checkbox(communication_tools, key=f'communication_tools_{communication_tools}'):
            selected_communication_tools.append(communication_tools)

# Submit button
if st.button('Recommend'):
    # You should process the inputs and generate recommendations here.
    st.write("Recommendations coming soon...")
    # Example: st.write(recommend_tech_talents(age, work_pref, education, ...))
