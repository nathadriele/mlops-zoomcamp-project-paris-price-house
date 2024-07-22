from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

def load_dataset(file_path):
    data = pd.read_csv(file_path)
    features = ['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors', 'cityCode', 'cityPartRange', 
                'numPrevOwners', 'made', 'isNewBuilt', 'hasStormProtector', 'basement', 'attic', 'garage', 
                'hasStorageRoom', 'hasGuestRoom']
    target = 'price'
    X = data[features]
    y = data[target]
    return X, y

def train_model(X_train, y_train):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    return model, scaler

file_path = "data/paris-housing.csv"
X, y = load_dataset(file_path)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model, scaler = train_model(X_train, y_train)

@app.route('/', methods=['GET'])
def home():
    return "API de Previsão de Preços Imobiliários em Paris"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        features = pd.DataFrame([data])
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        return jsonify({'predicted_price': prediction})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(debug=True)