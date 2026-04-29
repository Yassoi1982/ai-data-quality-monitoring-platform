import pandas as pd
from shared.python.data_quality_checks import run_data_quality_checks


def test_data_quality_checks():
    df = pd.DataFrame({
        "Time": [1, 2, 2],
        "Amount": [100, 200, 200],
        "Class": [0, 1, 1]
    })

    metrics = run_data_quality_checks(df)

    assert metrics["total_rows"] == 3
    assert metrics["duplicate_count"] == 1