import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()

    score = body.get("data_quality_score", 100)
    anomaly_count = body.get("anomaly_count", 0)
    threshold = body.get("threshold", 90)

    if score < threshold:
        status = "FAILED"
        message = f"Data quality score dropped to {score}. Threshold is {threshold}."
    else:
        status = "PASSED"
        message = f"Data quality score is healthy: {score}."

    result = {
        "alert_status": status,
        "message": message,
        "anomaly_count": anomaly_count
    }

    return func.HttpResponse(
        json.dumps(result),
        status_code=200,
        mimetype="application/json"
    )