import json
import pandas as pd
from shared.python.data_quality_checks import run_data_quality_checks
from shared.python.data_quality_score import calculate_data_quality_score
from shared.python.anomaly_detection import detect_anomalies


def lambda_handler(event, context):
    # Example mock data (later will come from S3)
    data = event.get("records", [])

    df = pd.DataFrame(data)

    metrics = run_data_quality_checks(df)
    score = calculate_data_quality_score(metrics)

    anomaly_df = detect_anomalies(df)
    anomaly_count = int(anomaly_df["anomaly_flag"].sum())

    result = {
        "metrics": metrics,
        "data_quality_score": score,
        "anomaly_count": anomaly_count
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }