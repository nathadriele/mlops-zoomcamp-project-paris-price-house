# MLOps Project `Property Price Forecast in Paris`

**Deployment URL**: https://vercel-app-mlops-zoomcamp-project-paris-price-house.vercel.app.

![gif](https://github.com/user-attachments/assets/9dc3cf89-8f41-470d-9008-83a695085926)

#

### About

This project focuses on predicting property prices in the urban environment of Paris based on various characteristics. The primary objective is to provide accurate price estimates for properties using machine learning models, aiding potential buyers, real estate agents, and developers in making informed decisions. The project is part of the MLOps Zoomcamp course by DataTalks.Club, designed to teach practical MLOps skills and methodologies for deploying and managing machine learning models at scale.

#

### Project Overview

This project aims to predict house prices in the urban environment of Paris using a variety of features. The primary goal is to provide accurate property price estimations through machine learning models. This information will assist potential buyers, real estate agents, and developers in making well-informed decisions.

#

![Captura de tela 2024-07-22 170053](https://github.com/user-attachments/assets/836c3ef3-d0c9-4afb-9258-79aa01db9f79)

### Dataset Description

The dataset used in this project consists of synthetic data on house prices in Paris. It includes numeric attributes representing various features of the properties. This dataset is particularly valuable for educational purposes, practice, and gaining knowledge in machine learning and data analysis.

The dataset can be found on Kaggle: [Paris Housing Price Prediction](https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction).

#### Context and Content do Dataset

This dataset is created from synthetic data representing house prices in the urban environment of Paris. It is ideal for educational purposes, practice, and gaining essential knowledge in machine learning and data analysis.

Next, the goal is to create a classification dataset from the existing data by adding a new column for the class attribute.

The dataset contains more than just rows and columns, it includes detailed house attributes listed as column names.

#### Description of Dataset Columns

All attributes are numeric variables and are listed below:

- `squareMeters`: Total area of the house in square meters.
- `numberOfRooms`: Total number of rooms in the house.
- `hasYard`: Indicates whether the house has a yard (1 for yes, 0 for no).
- `hasPool`: Indicates whether the house has a pool (1 for yes, 0 for no).
- `floors`: Number of floors in the house.
- `cityCode`: Zip code of the house's location.
- `cityPartRange`: A range value indicating the exclusivity of the neighborhood; higher values denote more exclusive areas.
- `numPrevOwners`: Number of previous owners the house has had.
- `made`: Year the house was built.
- `isNewBuilt`: Indicates whether the house is newly built (1 for yes, 0 for no).
- `hasStormProtector`: Indicates whether the house has storm protection features (1 for yes, 0 for no).
- `basement`: Area of the basement in square meters.
- `attic`: Area of the attic in square meters.
- `garage`: Size of the garage in square meters.
- `hasStorageRoom`: Indicates whether the house has a storage room (1 for yes, 0 for no).
- `hasGuestRoom`: Number of guest rooms in the house.
- `price`: Predicted price value of the house.

  - **Dataset Size**: ParisHousing.csv (633.42 kB)
  - **Tags**: Real Estate; Hotels and Accommodations; Regression; Cities and Urban Areas; Housing; Linear Regression
  - **Dataset available at Kaggle**: [Paris Housing Price Prediction](https://www.kaggle.com/datasets/mssmartypants/paris-housing-price-prediction)

#

### Prerequisites and Description of selected Frameworks and Tools

To successfully execute this MLOps project focused on predicting house prices in Paris, the following prerequisites and tools are required:

- `Git`: Used for version control to manage and track changes in the project codebase, facilitating collaboration and continuous integration.
- `GitHub`: Platforms for hosting Git repositories, enabling code collaboration, continuous integration (CI), and continuous deployment (CD).
- `Visual Studio Code`: An integrated development environment (IDE) used for debugging and managing Python code and other files, providing a robust environment for code development.
- `Jupyter Notebook`: An open-source web application used for data exploration, analysis, and visualization, allowing interactive development and testing of machine learning models.
- `PostgreSQL`: A powerful, open-source relational database management system used for storing and retrieving structured data, ensuring data persistence and integrity.
- `Anaconda`: A distribution of Python for scientific computing and data science, used for package management and creating virtual environments to manage dependencies.
- `Docker`: A platform used for containerization, enabling the application to run consistently across different environments by packaging all dependencies and configurations into a container.
- `Flask`: A lightweight web framework for Python, used for deploying the machine learning model as a web service, providing an API for interaction with the model.
- `Grafana`: An open-source platform for monitoring and observability, used for visualizing and monitoring the performance of the prediction model, ensuring its reliability and efficiency.
- `MLflow`: An open-source platform for managing the machine learning lifecycle, used for experiment tracking, model logging, and deployment, ensuring reproducibility and versioning of models.
- `Node.js`: For building scalable network applications, useful for developing the front-end interface or microservices in the project.
- `Prefect`: A workflow orchestration tool used for automating, scheduling, and monitoring data workflows, ensuring the smooth execution of data pipelines.
- `Pandas`: A data manipulation and analysis library for Python, used for handling structured data and performing exploratory data analysis (EDA).
- `Scikit-learn`: A machine learning library for Python, used for building, training, and evaluating the prediction model, providing various tools and algorithms for predictive modeling.
- `Matplotlib`: A plotting library for Python, used for data visualization to create static, interactive, and animated plots, helping in data analysis and presentation.
- `Vercel`: A cloud platform used for hosting and deploying web applications, ensuring the deployment and scalability of the project's web components.

#

### Paris Price House App

This is a Next.js and Python based ML application for house price prediction in Paris, France.

#

## Getting Started

### Prerequisites

* Node.js installed on your machine
* Python installed on your machine

#

### Installation

1. Create a new Next.js app using the latest version of `create-next-app`:
```
npx create-next-app@latest paris-price-house
```
2. Change into the newly created app directory:
```
cd paris-price-house
```
3. Install Axios, a popular HTTP client library:
```
npm install axios
```

### Running the App

1. Run the Python script that fetches data from an external API:
```
python app.py
```
2. Start the Next.js development server:
```
npx next
```
This will start the development server and make the app available at `http://localhost:3000`.

#

### Running the Project MLflow

![mlflow](https://github.com/user-attachments/assets/fe4f00e1-a100-4828-806c-31ae2bbf0773)

1. **Start MLflow Server**
 
Run the following command to start the MLflow server with a SQLite backend store and default artifact root:
```
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0
```
This will start the MLflow server, which will track experiments and store artifacts in the `mlruns` directory.

2. **Train Paris Housing Model**

Run the following command to train the Paris Housing model:
```
python train_paris_housing_model
```
This will train a machine learning model on the Paris Housing dataset and log the experiment to MLflow.

3. **Deploy Paris Housing API**

Run the following command to deploy the Paris Housing API:
```
python paris_housing_api
```
This will deploy a REST API that serves the trained model.

4. **Start Prefect Server**

Run the following command to start the Prefect server:
```
python prefect server start
```
This will start the Prefect server, which will schedule and run the Prefect flow.

5. **Run Paris Housing Prefect Flow**

Run the following command to run the Paris Housing Prefect flow:
```
python paris_housing_prefect_flow
```
This will schedule and run the Prefect flow, which will execute the trained model.

6. **Run Tests**

Run the following command to run tests for the Paris Housing API:
```
python tests/test_paris_housing_api
```
This will run tests to ensure the API is functioning correctly.

![prefect 2](https://github.com/user-attachments/assets/3cbd8e7c-fe19-4f22-9edf-8fe4af8278ba)

![prefect 1](https://github.com/user-attachments/assets/8adcb49b-3b9d-474e-a1fb-0e28bcbe528e)

#

### Model Execution Result

![model1](https://github.com/user-attachments/assets/522fee3c-ff6d-4099-adee-a75d578dec43)

![model2](https://github.com/user-attachments/assets/2ad679f2-5a27-4dd4-be31-01cc061026ce)

![model3](https://github.com/user-attachments/assets/a5919f7c-46bf-4bbf-b1f9-3c25cd80a8a4)

![model4](https://github.com/user-attachments/assets/3ef7f8a2-e29c-49e7-b8c6-6359279e5693)

![mode5](https://github.com/user-attachments/assets/784b3b9f-410e-4633-b5b9-273f0a9730cf)

![model6](https://github.com/user-attachments/assets/8df18004-0309-4a50-ab3a-c63f32dd2c2a)

![model7](https://github.com/user-attachments/assets/59ce62de-857f-47ff-8ce5-7899570c120c)

![mdel8](https://github.com/user-attachments/assets/7e79780c-7be1-47de-ba4f-14667b5ba182)

#

### Monitoring and Observability with Grafana

![grafana](https://github.com/user-attachments/assets/f77e9d99-1ff0-4897-be2d-1171b0101b85)

#

### Deployment vercel-app-mlops-zoomcamp-project-paris-price-house.vercel.app

![Captura de tela 2024-07-22 182910](https://github.com/user-attachments/assets/82243659-6852-4618-a66f-6d66b3f7c068)

The project is deployed on Vercel, making it easily accessible for users. The deployment ensures that users can input property details through the frontend and get real-time price predictions.

### How to Use app vercel Property Price Forecast in Paris

- 1. Fill in all fields with property information, enter information about the property in the input fields provided in the interface. Only positive numbers are allowed.
- 2. For fields where there is no information to be entered, they must be filled in with 0, indicating the absence.
- 3. If any field is not filled in, clicking the "Estimate Price" button will return the alert "Please fill in all fields to get a forecast!"
- 4. After filling in all the fields, click on the "Estimate Price" button to obtain the predicted price of the property.
- 5. View the results, the predicted price will be displayed on the screen, providing an estimate based on the input data. Example: "Forecasted Price: €557642.1".
- 6. Click on the "Clear Fields" button so that all fields are reset.
 
#

### Importance of the Project

Predicting property prices accurately is crucial for various stakeholders in the real estate market. This project leverages machine learning to provide reliable price estimates, which can help:

- Buyers: Make informed decisions about purchasing properties.
- Real Estate Agents: Provide accurate price recommendations to clients.
- Developers: Evaluate potential investments and project profitability. By using this project, users can gain insights into property pricing trends in Paris and make better financial decisions.

**This project serves as an excellent example of applying MLOps principles to a real-world problem, demonstrating the integration of data science, machine learning, and operational processes to deliver valuable insights and solutions**.

#

### Project Best Practices

- ✅ Problem description: The project is well described and it's clear and understandable. 
- ✅ Experiment tracking and model registry: Both experiment tracking and model registry are used.
- ✅ Workflow orchestration: Fully deployed workflow.
- ✅ Model deployment: The model deployment code is containerized and can be deployed to the cloud.
- ✅ Model monitoring: Basic model monitoring that calculates and reports metrics.
- ✅ Reproducibility: Instructions are clear, it's easy to run the code, and it works. The versions for all the dependencies are specified.
- ✅ Visualization: Visualization of the practical project in Vercel.

#

### Acknowledgments

This project was developed as part of the MLOps Zoomcamp course by DataTalks.Club. Special thanks to the course instructors and the community for their support and guidance.
