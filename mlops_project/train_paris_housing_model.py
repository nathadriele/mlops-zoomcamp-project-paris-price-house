import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import os

# Configuração do MLflow
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
EXPERIMENT_NAME = "Paris Housing Price Prediction - Enhanced"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment(EXPERIMENT_NAME)

def load_housing_data(file_path):
    """
    Carrega e prepara o dataset de habitação para treinamento.
    """
    housing_data = pd.read_csv(file_path)
    target_column = 'price'
    feature_columns = [col for col in housing_data.columns if col != target_column]
    return housing_data[feature_columns], housing_data[target_column]

def preprocess_features(features):
    """
    Pré-processa as features, incluindo one-hot encoding para variáveis categóricas.
    """
    # Converte variáveis booleanas para int
    bool_columns = ['hasYard', 'hasPool', 'isNewBuilt', 'hasStormProtector', 'hasStorageRoom', 'hasGuestRoom']
    features[bool_columns] = features[bool_columns].astype(int)
    
    # One-hot encoding para 'cityCode' e 'cityPartRange'
    features = pd.get_dummies(features, columns=['cityCode', 'cityPartRange'], prefix=['city', 'part'])
    
    return features

def normalize_features(features):
    """
    Normaliza as features numéricas usando StandardScaler.
    """
    feature_normalizer = StandardScaler()
    normalized_features = feature_normalizer.fit_transform(features)
    return normalized_features, feature_normalizer

def create_model(X_train, y_train):
    """
    Cria e treina o modelo Random Forest.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def calculate_model_metrics(model, X_test, y_test):
    """
    Calcula e retorna as métricas de desempenho do modelo.
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    return {"Mean Squared Error": mse, "Root Mean Squared Error": rmse, "R-squared": r2}

def main():
    data_file_path = "paris-housing.csv"
    
    # Carrega e divide o dataset
    features, target = load_housing_data(data_file_path)
    features_processed = preprocess_features(features)
    X_train, X_test, y_train, y_test = train_test_split(features_processed, target, test_size=0.2, random_state=42)
    
    # Inicia o experimento MLflow
    with mlflow.start_run() as mlflow_run:
        # Normalização
        X_train_norm, feature_normalizer = normalize_features(X_train)
        X_test_norm = feature_normalizer.transform(X_test)
        
        # Treinamento do modelo
        housing_model = create_model(X_train_norm, y_train)
        
        # Avaliação do modelo
        model_metrics = calculate_model_metrics(housing_model, X_test_norm, y_test)
        
        # Log de parâmetros, métricas e artefatos no MLflow
        mlflow.log_params({
            "model_type": "RandomForestRegressor",
            "n_estimators": 100,
            "normalizer": "StandardScaler",
            "features": features_processed.columns.tolist()
        })
        mlflow.log_metrics(model_metrics)
        mlflow.sklearn.log_model(housing_model, "housing_price_model")
        mlflow.sklearn.log_model(feature_normalizer, "feature_normalizer")
        
    print(f"Modelo treinado e registrado no MLflow com run_id: {mlflow_run.info.run_id}")
    print(f"Desempenho do modelo: {model_metrics}")

if __name__ == "__main__":
    main()