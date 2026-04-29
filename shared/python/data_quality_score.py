def calculate_data_quality_score(metrics: dict) -> float:
    total_rows = metrics.get("total_rows", 0)

    if total_rows == 0:
        return 0.0

    score = 100
    score -= (metrics.get("null_count", 0) / total_rows) * 100
    score -= (metrics.get("duplicate_count", 0) / total_rows) * 100
    score -= (metrics.get("invalid_amount_count", 0) / total_rows) * 100
    score -= (metrics.get("outlier_count", 0) / total_rows) * 50

    return round(max(score, 0), 2)