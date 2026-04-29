# AI Data Quality Monitoring Platform

End-to-end AI-driven data quality monitoring platform with:
- Data validation
- Data quality scoring
- Anomaly detection (ML)
- Dashboard (Streamlit)
- Multi-cloud structure (AWS, Azure, GCP)

## Run locally

```bash
pip install -r requirements.txt
py -m scripts.run_all_checks
streamlit run dashboard/app.py