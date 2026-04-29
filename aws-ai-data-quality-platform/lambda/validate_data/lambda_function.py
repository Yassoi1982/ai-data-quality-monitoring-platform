import json
from io import StringIO

import boto3
import pandas as pd

from shared.python.data_quality_checks import run_data_quality_checks
from shared.python.data_quality_score import calculate_data_quality_score


s3 = boto3.client("s3")


def lambda_handler(event, context):
    bucket = event["bucket"]
    key = event["key"]

    obj = s3.get_object(Bucket=bucket, Key=key)
    csv_content = obj["Body"].read().decode("utf-8")

    df = pd.read_csv(StringIO(csv_content))

    metrics = run_data_quality_checks(df)
    score = calculate_data_quality_score(metrics)

    return {
        "statusCode": 200,
        "bucket": bucket,
        "key": key,
        "metrics": metrics,
        "data_quality_score": score
    }