# Logic Apps Deployment Guide

## Workflow

Blob upload → Validate Data Function → Detect Anomalies Function → Send Alert Function

## Steps

1. Create Logic App
2. Add Blob Storage trigger
3. Add HTTP action for validate_data
4. Add HTTP action for detect_anomalies
5. Add HTTP action for send_alert
6. Save and test workflow