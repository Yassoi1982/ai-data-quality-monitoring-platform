import os
import boto3


sns = boto3.client("sns")


def lambda_handler(event, context):
    score = event.get("data_quality_score", 100)
    anomaly_count = event.get("anomaly_count", 0)
    threshold = event.get("threshold", 90)

    topic_arn = os.environ.get("SNS_TOPIC_ARN")

    if score < threshold:
        status = "FAILED"
        message = (
            f"Data Quality Alert\n\n"
            f"Status: FAILED\n"
            f"Data Quality Score: {score}\n"
            f"Threshold: {threshold}\n"
            f"Anomaly Count: {anomaly_count}"
        )
    else:
        status = "PASSED"
        message = (
            f"Data Quality Check Passed\n\n"
            f"Status: PASSED\n"
            f"Data Quality Score: {score}\n"
            f"Threshold: {threshold}\n"
            f"Anomaly Count: {anomaly_count}"
        )

    if topic_arn:
        sns.publish(
            TopicArn=topic_arn,
            Subject=f"AI Data Quality Monitoring - {status}",
            Message=message
        )

    return {
        "statusCode": 200,
        "alert_status": status,
        "message": message
    }