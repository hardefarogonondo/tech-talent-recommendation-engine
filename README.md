# tech-talent-recommendation-engine

# Food.com Recipe Recommendation Engine

A Machine learning-based tech talent recommendation engine that matches developers with job roles using insights from Stack Overflow data.

## Table of Contents

1. [Project Description](#project-description)
2. [Project Architecture](#project-architecture)
3. [Installation Guide](#installation-guide)
4. [Dataset Information](#dataset-information)
5. [Conclusions](#conclusions)
6. [Future Works](#future-works)
7. [References](#references)

## Project Description

Our project introduces a custom-built recommendation engine, enhancing tech career matchmaking by harnessing insights from the Stack Overflow Developer Survey 2023. With an advanced machine learning library, our engine employs Alternating Least Squares (ALS) and Gradient Descent methods to accurately predict job compatibility, focusing on the rich spectrum of developer skills.

Evaluating our model's performance through Mean Square Error (MSE) and Mean Absolute Error (MAE), we ensure precise and reliable recommendations. This entire solution is elegantly packaged using Docker, facilitating a seamless setup and user experience. Dive into our repository to see the intersection of data science and human resource innovation in action.

## Project Architecture

The project's architecture has a structured folder layout for better organization and accessibility. The root directory consists of several sub-folders each dedicated for specific purposes. The project's folder structure would look like this:

```bash
.
├── data
│   ├── processed
│   └── raw
├── models
├── notebooks
│   ├── 1_data_preparation
│   ├── 2_exploratory_data_analysis_and_preprocessing
│   ├── 3_feature_engineering
│   └── 4_model_training_and_evaluation
├── references
├── reports
│   └── figures
└── src
    ├── back_end
    └── front_end
```

## Installation Guide

This project utilizes Docker to manage the service environment. Here's a step-by-step guide to build the Docker image, create the Docker container, and run the service:

### Build The Docker Image

Open your terminal in the project root directory, and run the following command to build the Docker image:

```bash
docker-compose build
```

### Create The Docker Container

Now, let's create a Docker container from the image we just built. Run the following command:

```bash
docker-compose up
```

Upon successfully creating the Docker container, your service should automatically be up and running. You can access it through the localhost port on your web browser via this [URL](http://localhost:8501/):

```bash
http://localhost:8501/
```

If you want to stop the service for any reason, you can press <kbd>CTRL</kbd> + <kbd>C</kbd> in your current terminal or use the following command in another terminal:

```bash
docker-compose down
```

### Run the Service

To start the service, use the following command in your terminal:

```bash
docker-compose up
```

You can now access the front-end of the service through the localhost port on your web browser via this [URL](http://localhost:8501/):

```bash
http://localhost:8501/
```

To use the service, simply choose a User ID from the drop-down menu and click the 'Submit' button. The engine will then display recipes that the selected user has previously rated, along with new recipe recommendations for the user to rate next.

### API Details

#### Fetching Available User IDs

To get a list of available user IDs for making recommendations, send a GET request to the following endpoint:

```bash
http://backend:8000/available_users
```

#### API Response Format

The API will respond with a list of available user IDs in the following JSON format:

```json
{
  "age_range": "Under 18 years old",
  "work_arrangement": "Remote",
  "education_level": "Primary/elementary school",
  "role": "Academic researcher",
  "years_of_experience": 0,
  "programming_languages": "",
  "databases": "",
  "cloud_platforms": "",
  "web_frameworks": "",
  "other_frameworks": "",
  "developer_tools": "",
  "development_environments": "",
  "operating_systems": "",
  "collaboration_tools": "",
  "communication_tools": "Zoom;Zulip"
}
```

#### Fetching Recipe Recommendations for a User

To get past rated recipes and new recipe recommendations for a specific user, send a GET request to this endpoint:

```bash
http://backend:8000/recommend/{user_id}
```

Replace <kbd>{user_id}</kbd> with the actual user ID you are interested in.

#### API Response Format

The API will respond with the user's past rated recipes and new recipe recommendations in the following format:

```json
{
    "recommended_candidates": [
        {
            "ResponseId": 39405,
            "Age": "18-24 years old",
            "RemoteWork": "Hybrid (some remote, some in-person)",
            "EdLevel": "Some college/university study without earning a degree",
            "YearsCode": 8.0,
            "DevType": "Developer, full-stack",
            "Country": "Sweden",
            "LanguageHaveWorkedWith": "Bash/Shell (all shells);C#;HTML/CSS;JavaScript;PHP;PowerShell;Python;SQL;TypeScript",
            "DatabaseHaveWorkedWith": "Microsoft SQL Server;PostgreSQL",
            "PlatformHaveWorkedWith": "Microsoft Azure",
            "WebframeHaveWorkedWith": "Angular;ASP.NET;ASP.NET CORE;jQuery;Node.js;React;Vue.js;WordPress",
            "MiscTechHaveWorkedWith": ".NET (5+) ;.NET Framework (1.0 - 4.8)",
            "ToolsTechHaveWorkedWith": "Docker;MSBuild;npm;NuGet;Visual Studio Solution;Vite;Webpack",
            "NEWCollabToolsHaveWorkedWith": "Visual Studio;Visual Studio Code",
            "OpSysPersonal use": "Windows",
            "OfficeStackAsyncHaveWorkedWith": "Azure Devops;Markdown File",
            "OfficeStackSyncHaveWorkedWith": "Discord;Microsoft Teams"
        },
        {
            "ResponseId": 16435,
            "Age": "25-34 years old",
            "RemoteWork": "Hybrid (some remote, some in-person)",
            "EdLevel": "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)",
            "YearsCode": 12.0,
            "DevType": "Developer, full-stack",
            "Country": "France",
            "LanguageHaveWorkedWith": "C#;HTML/CSS;JavaScript;PowerShell;SQL;TypeScript;Visual Basic (.Net)",
            "DatabaseHaveWorkedWith": "Microsoft SQL Server;MySQL;Oracle;SQLite",
            "PlatformHaveWorkedWith": "Microsoft Azure",
            "WebframeHaveWorkedWith": "Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js",
            "MiscTechHaveWorkedWith": ".NET (5+) ;.NET Framework (1.0 - 4.8)",
            "ToolsTechHaveWorkedWith": "Chocolatey;Docker;MSBuild;npm;NuGet;Unity 3D;Visual Studio Solution;Webpack",
            "NEWCollabToolsHaveWorkedWith": "Notepad++;Visual Studio;Visual Studio Code",
            "OpSysPersonal use": "Windows",
            "OfficeStackAsyncHaveWorkedWith": "Azure Devops;Jira",
            "OfficeStackSyncHaveWorkedWith": "Discord;Microsoft Teams"
        },
    ...
}
```

Simply use Postman to send these GET requests to the mentioned endpoints and you will receive the data in the mentioned formats.

## Dataset Information

The dataset leveraged for this project comes from Food.com (formerly GeniusKitchen). This extensive dataset contains over 180K recipes and 700K recipe reviews, spanning 18 years of user interactions and uploads.

Key files used in our project from this dataset include:

- `RAW_interactions.csv`: Contains user interactions, including recipe reviews and ratings.
- `RAW_recipes.csv`: Contains details of the recipes.

For more in-depth information, a detailed document describing the dataset is available [here](references/DATASET.md).

## Conclusions

- Due to computational limitations, the dataset was narrowed to include only the last 3 years of data.
- Both SVD and KNN algorithms were explored. KNN was ultimately selected for its superior performance in RMSE metrics.
- No hyperparameter tuning was carried out to optimize the models further.
- The feature used for making recommendations was the explicit data—user ratings. A user-item matrix was developed for this purpose.
- A front-end was created specifically for administrators, displaying past rated and recommended recipes for each registered user.
- Both front-end and back-end services were containerized using Docker, enhancing maintainability.
- While the project has not been deployed yet, the recommendation engine has the potential to significantly improve user engagement and increase key metrics like User Retention and Repeat Visitor Rate.

## Future Works

- Expand the dataset to include a broader timeframe, improving the model's comprehensiveness.
- Incorporate more personalized features, potentially leveraging implicit data for more accurate recommendations.
- Investigate the use of advanced modeling techniques to improve the system's recommendation capabilities.
- Improve the user interface to allow users to directly view personalized recommendations on their account pages.
- Enhance the administrator UI for a more intuitive understanding of user recommendations.
- Optimize Docker setup for resource efficiency and quicker startup times.

## Medium Articles

[Recipe for Retention: How a Data-Driven Recommendation Engine is Spicing Up User Engagement for Food.com](https://medium.com/@hardefarogonondo/recipe-for-retention-how-a-data-driven-recommendation-engine-is-spicing-up-user-engagement-for-518fe347a3dd)

## Acknowledgment: Pacmann Student Hackathon 2023

This project was developed as part of the Pacmann Student Hackathon 2023, a competitive and enriching event that brought together talented data scientists and developers.

We're absolutely thrilled to announce that our project not only received the Best Presentation Award but also secured the 1st Winner in the Pacmann Student Hackathon 2023. This accolade is a testament to the hard work, dedication, and skill of our incredible team.

We'd like to express our deepest gratitude to the hackathon organizers, judges, and fellow participants. It was an enriching experience to compete against such talented individuals, and we learned a lot along the journey.

Thank you for making this event a challenging yet rewarding experience!

![1st Winner and Best Presentation Award](reports/figures/1st_winner_and_best_presentation_award.jpg)

## References

This section lists all the references and resources utilized during the project.

[1] [Generating Personalized Recipes from Historical User Preferences](https://aclanthology.org/D19-1613/)

[2] [ML-Based Collaborative Filtering for Cross-Cultural Music Recommendations](https://cs229.stanford.edu/proj2021spr/report2/82006572.pdf)

[3] [FastAPI](https://fastapi.tiangolo.com/)

[4] [Streamlit](https://streamlit.io/)

[5] [Docker](https://www.docker.com/)
