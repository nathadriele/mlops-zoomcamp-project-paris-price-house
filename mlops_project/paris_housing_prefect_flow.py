from prefect import flow, task
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pandas as pd
import os
import mlflow
import mlflow.sklearn

@task
def load_housing_data(file_path):
    housing_data = pd.read_csv(file_path)
    target_column = 'price'
    feature_columns = [col for col in housing_data.columns if col != target_column]
    return housing_data[feature_columns], housing_data[target_column]

@task
def preprocess_features(features):
    bool_columns = ['hasYard', 'hasPool', 'isNewBuilt', 'hasStormProtector', 'hasStorageRoom', 'hasGuestRoom']
    features[bool_columns] = features[bool_columns].astype(int)
    features = pd.get_dummies(features, columns=['cityCode', 'cityPartRange'], prefix=['city', 'part'])
    return features

@task
def normalize_features(features):
    feature_normalizer = StandardScaler()
    normalized_features = feature_normalizer.fit_transform(features)
    return normalized_features, feature_normalizer

@task
def train_housing_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

@flow(name="paris-house-price-prediction")
def paris_house_price_prediction_flow():
    # Configuração do MLflow
    MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
    EXPERIMENT_NAME = "Paris Housing Price Prediction - Prefect Flow"
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)

    data_file_path = os.path.join(os.path.dirname(__file__), "data/paris-housing.csv")
    features, target = load_housing_data(data_file_path)
    
    features_processed = preprocess_features(features)
    X_train, X_test, y_train, y_test = train_test_split(features_processed, target, test_size=0.2, random_state=42)
    
    X_train_norm, feature_normalizer = normalize_features(X_train)
    
    with mlflow.start_run() as run:
        model = train_housing_model(X_train_norm, y_train)
        
        # Log de parâmetros e modelo no MLflow
        mlflow.log_params({
            "model_type": "RandomForestRegressor",
            "n_estimators": 100,
            "normalizer": "StandardScaler",
            "features": features_processed.columns.tolist()
        })
        mlflow.sklearn.log_model(model, "paris_housing_price_model")
        mlflow.sklearn.log_model(feature_normalizer, "feature_normalizer")
        
        print(f"Modelo treinado e registrado no MLflow com run_id: {run.info.run_id}")
    
    return model, feature_normalizer

if __name__ == "__main__":
    paris_house_price_prediction_flow()