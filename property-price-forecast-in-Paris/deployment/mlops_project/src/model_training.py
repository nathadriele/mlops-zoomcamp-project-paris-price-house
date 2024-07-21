import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

def train_model(X_train, y_train):
    with mlflow.start_run():
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train)
        
        mlflow.log_param("n_estimators", 100)
        mlflow.sklearn.log_model(model, "model")
        
        return model, scaler
