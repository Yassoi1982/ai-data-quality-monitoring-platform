from shared.python.anomaly_detection import detect_anomalies
import pandas as pd
from google.cloud import storage
from io import StringIO

def detect_anomalies_func(request):
    request_json = request.get_json()

    bucket_name = request_json["bucket"]
    file_name = request_json["file"]

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    data = blob.download_as_text()
    df = pd.read_csv(StringIO(data))

    anomaly_df = detect_anomalies(df)
    anomaly_count = int(anomaly_df["anomaly_flag"].sum())

    return {"anomaly_count": anomaly_count}