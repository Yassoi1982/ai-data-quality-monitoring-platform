import pandas as pd


def run_data_quality_checks(df: pd.DataFrame) -> dict:
    total_rows = len(df)

    return {
        "total_rows": total_rows,
        "null_count": int(df.isnull().sum().sum()),
        "duplicate_count": int(df.duplicated().sum()),
        "invalid_amount_count": int((df["Amount"] < 0).sum()),
        "outlier_count": int(
            (df["Amount"] > df["Amount"].mean() + 3 * df["Amount"].std()).sum()
        ),
    }