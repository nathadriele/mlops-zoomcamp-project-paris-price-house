from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
import pickle
import os
import pandas as pd
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Configuração do MLflow
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
MODEL_RUN_ID = "7472c91377c24f92ac7d81c1b7d4cb89"
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
housing_model = mlflow.sklearn.load_model(f'runs:/{MODEL_RUN_ID}/housing_price_model')

# Carregar o normalizador
NORMALIZER_PATH = os.path.join(os.path.dirname(__file__), "feature_normalizer.pkl")
with open(NORMALIZER_PATH, "rb") as normalizer_file:
    feature_normalizer = pickle.load(normalizer_file)

# Configuração do PostgreSQL
DB_CONFIG = {
    'host': 'localhost',
    'database': 'test',
    'user': 'postgres',
    'password': '3099'
}

def get_database_connection():
    return psycopg2.connect(**DB_CONFIG)

def log_prediction_metrics(request_count, request_latency):
    with get_database_connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO prediction_metrics (request_count, request_latency, timestamp)
            VALUES (%s, %s, %s);
        """, (request_count, request_latency, datetime.now()))

def preprocess_features(features_dict):
    features_df = pd.DataFrame([features_dict])
    bool_columns = ['hasYard', 'hasPool', 'isNewBuilt', 'hasStormProtector', 'hasStorageRoom', 'hasGuestRoom']
    features_df[bool_columns] = features_df[bool_columns].astype(int)
    
    # One-hot encoding para 'cityCode' e 'cityPartRange'
    features_df = pd.get_dummies(features_df, columns=['cityCode', 'cityPartRange'], prefix=['city', 'part'])
    
    # Garantir que todas as colunas esperadas estejam presentes
    expected_columns = feature_normalizer.feature_names_in_
    for col in expected_columns:
        if col not in features_df.columns:
            features_df[col] = 0
    
    return features_df[expected_columns]

def normalize_features(features):
    return feature_normalizer.transform(features)

def predict_price(features):
    preprocessed_features = preprocess_features(features)
    normalized_features = normalize_features(preprocessed_features)
    return housing_model.predict(normalized_features)[0]

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    start_time = datetime.now()
    try:
        data = request.get_json()
        predicted_price = predict_price(data)
        request_latency = (datetime.now() - start_time).total_seconds()
        log_prediction_metrics(1, request_latency)
        return jsonify({'predicted_price': float(predicted_price)})
    except (KeyError, TypeError) as e:
        return jsonify({'error': f'Dados de entrada inválidos: {str(e)}'}), 400

def initialize_database():
    with get_database_connection() as conn, conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prediction_metrics (
                id SERIAL PRIMARY KEY,
                request_count INTEGER,
                request_latency FLOAT,
                timestamp TIMESTAMP
            );
        """)

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True, host='0.0.0.0', port=9696)