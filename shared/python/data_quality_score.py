def calculate_data_quality_score(metrics: dict) -> float:
    total_rows = metrics.get("total_rows", 0)

    if total_rows == 0:
        return 0.0

    null_penalty = (metrics.get("null_count", 0) / total_rows) * 100
    duplicate_penalty = (metrics.get("duplicate_count", 0) / total_rows) * 100
    invalid_penalty = (metrics.get("invalid_amount_count", 0) / total_rows) * 100
    outlier_penalty = (metrics.get("outlier_count", 0) / total_rows) * 50

    score = 100 - null_penalty - duplicate_penalty - invalid_penalty - outlier_penalty

    return round(max(score, 0), 2)