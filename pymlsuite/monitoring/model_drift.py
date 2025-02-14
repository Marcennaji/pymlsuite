import mlflow
import pandas as pd
from sklearn.metrics import accuracy_score


def check_model_drift():
    old_model = mlflow.sklearn.load_model("mlruns/0/latest_model")
    new_data = pd.read_csv("datasets/new_batch.csv")
    X_new, y_new = new_data.drop(columns=["target"]), new_data["target"]

    predictions = old_model.predict(X_new)
    accuracy = accuracy_score(y_new, predictions)

    if accuracy < 0.85:  # Example threshold
        print("🚨 Model performance degraded! Retraining required.")
        trigger_retraining()


def trigger_retraining():
    print("🔄 Retraining the model...")
    # Call model training script
