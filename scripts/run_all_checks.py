# ##Counted Metric
# # # import pandas as pd

# # df = pd.read_csv("datasets/creditcard.csv")

# # print("Rows:", len(df))
# # print("Nulls:", df.isnull().sum().sum())
# # print("Duplicates:", df.duplicated().sum())

# # import pandas as pd
# # from shared.python.data_quality_checks import run_data_quality_checks

# # df = pd.read_csv("datasets/creditcard.csv")

# # metrics = run_data_quality_checks(df)

# # print("Data Quality Metrics:")
# # print(metrics)

# ##Added Score
# # import pandas as pd
# # from shared.python.data_quality_checks import run_data_quality_checks
# # from shared.python.data_quality_score import calculate_data_quality_score

# # df = pd.read_csv("datasets/creditcard.csv")

# # metrics = run_data_quality_checks(df)
# # score = calculate_data_quality_score(metrics)

# # print("\nData Quality Metrics:")
# # print(metrics)

# # print("\nData Quality Score:")
# # print(score)

# # Added Anaomaly Count 

# import pandas as pd
# from shared.python.data_quality_checks import run_data_quality_checks
# from shared.python.data_quality_score import calculate_data_quality_score
# from shared.python.anomaly_detection import detect_anomalies

# df = pd.read_csv("datasets/creditcard.csv")

# metrics = run_data_quality_checks(df)
# score = calculate_data_quality_score(metrics)

# anomaly_df = detect_anomalies(df)
# anomaly_count = int(anomaly_df["anomaly_flag"].sum())

# print("\nData Quality Metrics:")
# print(metrics)

# print("\nData Quality Score:")
# print(score)

# print("\nAnomaly Count:")
# print(anomaly_count)

import pandas as pd
from shared.python.data_quality_checks import run_data_quality_checks
from shared.python.data_quality_score import calculate_data_quality_score
from shared.python.anomaly_detection import detect_anomalies

df = pd.read_csv("datasets/creditcard.csv")

metrics = run_data_quality_checks(df)
score = calculate_data_quality_score(metrics)

anomaly_df = detect_anomalies(df)
anomaly_count = int(anomaly_df["anomaly_flag"].sum())

# Combine results
summary = {
    **metrics,
    "data_quality_score": score,
    "anomaly_count": anomaly_count
}

print("\nFinal Summary:")
print(summary)

# Save to CSV
pd.DataFrame([summary]).to_csv("outputs/data_quality_report.csv", index=False)

print("\nReport saved to outputs/data_quality_report.csv")