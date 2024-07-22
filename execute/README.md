**README.md**

**Project Overview**
================

This project is a machine learning workflow that trains a model on the Paris Housing dataset, deploys an API, and schedules a Prefect flow to run the model. The project uses MLflow to track experiments and store artifacts.

**Getting Started**
---------------

### Prerequisites

* Python 3.x
* MLflow
* Prefect
* SQLite

### Running the Project

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