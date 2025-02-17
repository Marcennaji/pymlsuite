import os
import mlflow
import khiops
import pandas as pd
import joblib
import logging
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Configuration
DATA_PATH = "datasets/train.csv"
MODEL_PATH = "pymlsuite/model/"
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"  # Change if using remote MLflow

# Ensure model directory exists
os.makedirs(MODEL_PATH, exist_ok=True)

# Set MLflow tracking URI
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)


# Load dataset
def load_data():
    logger.info("Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["target"])
    y = df["target"]
    return train_test_split(X, y, test_size=0.2, random_state=42)


# Train Khiops Model
def train_khiops(X_train, y_train):
    logger.info("Training Khiops model...")
    khiops_model_path = os.path.join(MODEL_PATH, "khiops_model.khj")
    df_train = X_train.copy()
    df_train["target"] = y_train

    khiops.train_model(khiops_model_path, df_train)

    # Logging to MLflow
    mlflow.log_param("model", "Khiops")
    mlflow.log_artifact(khiops_model_path)
    logger.info(f"Khiops model saved at {khiops_model_path}")


# Train Scikit-learn RandomForest
def train_random_forest(X_train, X_test, y_train, y_test):
    logger.info("Training RandomForest model...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    # Evaluate
    y_pred = rf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Save model
    rf_model_path = os.path.join(MODEL_PATH, "random_forest.pkl")
    joblib.dump(rf, rf_model_path)

    # Log metrics to MLflow
    with mlflow.start_run():
        mlflow.log_param("model", "RandomForest")
        mlflow.log_metric("accuracy", acc)
        mlflow.log_artifact(rf_model_path)

    logger.info(f"RandomForest model saved at {rf_model_path}, Accuracy: {acc}")


# Train XGBoost Model
def train_xgboost(X_train, X_test, y_train, y_test):
    logger.info("Training XGBoost model...")
    xgb = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    xgb.fit(X_train, y_train)

    # Evaluate
    y_pred = xgb.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    # Save model
    xgb_model_path = os.path.join(MODEL_PATH, "xgboost.pkl")
    joblib.dump(xgb, xgb_model_path)

    # Log metrics to MLflow
    with mlflow.start_run():
        mlflow.log_param("model", "XGBoost")
        mlflow.log_metric("accuracy", acc)
        mlflow.log_artifact(xgb_model_path)

    logger.info(f"XGBoost model saved at {xgb_model_path}, Accuracy: {acc}")


if __name__ == "__main__":
    # Load data
    X_train, X_test, y_train, y_test = load_data()

    # Train models
    train_khiops(X_train, y_train)
    train_random_forest(X_train, X_test, y_train, y_test)
    train_xgboost(X_train, X_test, y_train, y_test)

    logger.info("All models trained successfully.")
