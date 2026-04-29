import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import pandas as pd
import streamlit as st
from shared.python.data_quality_checks import run_data_quality_checks
from shared.python.data_quality_score import calculate_data_quality_score
from shared.python.anomaly_detection import detect_anomalies

st.set_page_config(
    page_title="AI Data Quality Monitoring Platform",
    layout="wide"
)

st.title("AI Data Quality Monitoring Platform")

uploaded_file = st.file_uploader("Upload creditcard.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    metrics = run_data_quality_checks(df)
    score = calculate_data_quality_score(metrics)

    anomaly_df = detect_anomalies(df)
    anomaly_count = int(anomaly_df["anomaly_flag"].sum())

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Rows", metrics["total_rows"])
    col2.metric("Null Count", metrics["null_count"])
    col3.metric("Duplicate Count", metrics["duplicate_count"])
    col4.metric("Data Quality Score", score)

    st.subheader("Anomaly Detection")
    st.metric("Anomaly Count", anomaly_count)

    st.subheader("Full Data Quality Summary")
    st.json({
        **metrics,
        "data_quality_score": score,
        "anomaly_count": anomaly_count
    })
else:
    st.info("Upload your Kaggle creditcard.csv file to begin.")