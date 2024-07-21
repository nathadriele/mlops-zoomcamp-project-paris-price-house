from prefect import flow, task
from src.data_preprocessing import load_dataset
from src.model_training import train_model

@task
def load_data_task(file_path):
    return load_dataset(file_path)

@task
def train_model_task(X_train, y_train):
    return train_model(X_train, y_train)

@flow
def house_price_prediction_flow(file_path: str):
    X_train, X_test, y_train, y_test = load_data_task(file_path)
    model, scaler = train_model_task(X_train, y_train)
    return model, scaler

if __name__ == "__main__":
    file_path = "data/paris-housing.csv"
    house_price_prediction_flow(file_path)

