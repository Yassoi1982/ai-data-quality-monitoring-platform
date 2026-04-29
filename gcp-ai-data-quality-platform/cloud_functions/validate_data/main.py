import pandas as pd
from google.cloud import storage
from io import StringIO
from shared.python.data_quality_checks import run_data_quality_checks
from shared.python.data_quality_score import calculate_data_quality_score

def validate_data(request):
    request_json = request.get_json()

    bucket_name = request_json["bucket"]
    file_name = request_json["file"]

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    data = blob.download_as_text()
    df = pd.read_csv(StringIO(data))

    metrics = run_data_quality_checks(df)
    score = calculate_data_quality_score(metrics)

    return {"metrics": metrics, "data_quality_score": score}