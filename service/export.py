import os

import mlflow
from mlflow import MlflowClient

mlflow.artifacts.download_artifacts("models:/complaint-router@champion", dst_path="service/model")
print(MlflowClient().get_model_version_by_alias("complaint-router", "champion").version)
print(sorted(os.listdir("service/model")))