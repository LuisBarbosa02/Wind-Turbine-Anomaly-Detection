# Import libraries
import mlflow
import pickle
from ..data.load_data import load_data
from ..config import PREPROCESSOR_PATH, MODEL_PATH
from ..model.train_model import model_parameters
from ..evaluation.evaluator import make_evaluation

# MLflow experiment
def run_experiment():
    # Set experiment in Databricks
    mlflow.set_tracking_uri("databricks")
    mlflow.set_experiment('/Shared/wind turbine anomaly')

    # Load data
    (_, X_test, _, y_test) = load_data()

    # Load preprocessor
    with open(PREPROCESSOR_PATH, 'rb') as file:
        preprocessor = pickle.load(file)

    # Load model
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)

    # Run experiment
    with mlflow.start_run() as run:
        # Log parameters
        mlflow.log_params(model_parameters)

        # Log metrics
        metrics = make_evaluation(preprocessor, model, X_test, y_test)
        mlflow.log_metrics(metrics)

        # Log model
        mlflow.sklearn.log_model(
            model,
            input_example=X_test,
            name="iso_for",
        )

# Run experiment
if __name__ == '__main__':
    run_experiment()