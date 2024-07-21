from flask import Flask, request, jsonify
from flask_cors import CORS
import mlflow.pyfunc
import pandas as pd

app = Flask(__name__)
CORS(app)

model = mlflow.pyfunc.load_model("models:/house-price-model/production")

@app.route('/', methods=['GET'])
def home():
    return "API de Previsão de Preços Imobiliários em Paris"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        features = pd.DataFrame([data])
        prediction = model.predict(features)[0]
        return jsonify({'predicted_price': prediction})
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid input data'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
