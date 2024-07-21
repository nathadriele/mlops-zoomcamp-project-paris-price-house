import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("house_price_prediction")

def load_data():
    data = pd.read_csv("data/paris-housing.csv")
    features = ['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors', 'cityCode', 'cityPartRange', 
                'numPrevOwners', 'made', 'isNewBuilt', 'hasStormProtector', 'basement', 'attic', 'garage', 
                'hasStorageRoom', 'hasGuestRoom']
    X = data[features]
    y = data['price']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model():
    X_train, X_test, y_train, y_test = load_data()
    
    with mlflow.start_run():
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Model trained. MSE: {mse}, R2: {r2}")
        
        return model

if __name__ == "__main__":
    train_model()