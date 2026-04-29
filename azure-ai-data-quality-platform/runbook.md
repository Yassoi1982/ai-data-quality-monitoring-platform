
### `runbook.md`

```md
# Azure Pipeline Runbook

## Steps

1. Upload `creditcard.csv` to Azure Blob Storage.
2. Run `validate_data` Azure Function.
3. Run `detect_anomalies` Azure Function.
4. Run `send_alert` Azure Function.
5. Monitor execution in Azure Monitor.
6. Capture screenshots for GitHub and resume.