import json
from io import StringIO

import boto3
import pandas as pd

from shared.python.anomaly_detection import detect_anomalies


s3 = boto3.client("s3")


def lambda_handler(event, context):
    bucket = event["bucket"]
    key = event["key"]

    obj = s3.get_object(Bucket=bucket, Key=key)
    csv_content = obj["Body"].read().decode("utf-8")

    df = pd.read_csv(StringIO(csv_content))

    anomaly_df = detect_anomalies(df)
    anomaly_count = int(anomaly_df["anomaly_flag"].sum())

    return {
        "statusCode": 200,
        "bucket": bucket,
        "key": key,
        "anomaly_count": anomaly_count
    }