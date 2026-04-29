import json
import pandas as pd
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from io import StringIO

from shared.python.data_quality_checks import run_data_quality_checks
from shared.python.data_quality_score import calculate_data_quality_score


def main(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()

    connection_string = body["azure_storage_connection_string"]
    container_name = body["container_name"]
    blob_name = body["blob_name"]

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    csv_data = blob_client.download_blob().readall().decode("utf-8")
    df = pd.read_csv(StringIO(csv_data))

    metrics = run_data_quality_checks(df)
    score = calculate_data_quality_score(metrics)

    result = {
        "metrics": metrics,
        "data_quality_score": score
    }

    return func.HttpResponse(
        json.dumps(result),
        status_code=200,
        mimetype="application/json"
    )