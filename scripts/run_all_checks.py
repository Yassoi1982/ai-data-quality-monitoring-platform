import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))
import pandas as pd
from shared.python.data_quality_checks import run_data_quality_checks
from shared.python.data_quality_score import calculate_data_quality_score
from shared.python.anomaly_detection import detect_anomalies


df = pd.read_csv("datasets/creditcard.csv")

metrics = run_data_quality_checks(df)
score = calculate_data_quality_score(metrics)

anomaly_df = detect_anomalies(df)
anomaly_count = int(anomaly_df["anomaly_flag"].sum())

summary = {
    **metrics,
    "data_quality_score": score,
    "anomaly_count": anomaly_count
}

print("\nFinal Data Quality Summary:")
print(summary)

pd.DataFrame([summary]).to_csv("outputs/data_quality_report.csv", index=False)

print("\nReport saved to outputs/data_quality_report.csv")