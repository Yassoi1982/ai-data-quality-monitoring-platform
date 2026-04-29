from shared.python.data_quality_score import calculate_data_quality_score


def test_score_is_between_0_and_100():
    metrics = {
        "total_rows": 100,
        "null_count": 5,
        "duplicate_count": 5,
        "invalid_amount_count": 0,
        "outlier_count": 2
    }

    score = calculate_data_quality_score(metrics)

    assert 0 <= score <= 100