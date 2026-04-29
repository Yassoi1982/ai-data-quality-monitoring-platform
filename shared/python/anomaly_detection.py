import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    features = ["Time", "Amount"]

    model = IsolationForest(
        n_estimators=100,
        contamination=0.01,
        random_state=42
    )

    result_df = df.copy()
    result_df["anomaly_flag"] = model.fit_predict(result_df[features])
    result_df["anomaly_flag"] = result_df["anomaly_flag"].map({1: 0, -1: 1})

    return result_df