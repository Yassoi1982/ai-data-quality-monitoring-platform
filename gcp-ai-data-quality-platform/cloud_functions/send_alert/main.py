def send_alert(request):
    request_json = request.get_json()

    score = request_json.get("data_quality_score", 100)
    threshold = request_json.get("threshold", 90)

    if score < threshold:
        status = "FAILED"
    else:
        status = "PASSED"

    return {
        "alert_status": status,
        "message": f"Score: {score}, Threshold: {threshold}"
    }