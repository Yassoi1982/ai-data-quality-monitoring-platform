# GCP Pipeline Runbook

## Steps

1. Upload `creditcard.csv` to Cloud Storage bucket
2. Deploy Cloud Functions:
   - validate_data
   - detect_anomalies
   - send_alert
3. Deploy Workflows
4. Trigger workflow execution
5. Monitor execution in Logs Explorer

## Expected Output

- Data quality score
- Anomaly count
- Alert status

## Debugging

Check:
- Function logs
- Workflow execution steps
- Storage access permissions