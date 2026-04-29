# GCP Architecture

```text
User Upload CSV → Cloud Storage
                     ↓
         Cloud Function: Validate Data
                     ↓
         Cloud Function: Detect Anomalies
                     ↓
         Cloud Function: Send Alert
                     ↓
              GCP Workflows
                     ↓
             Cloud Logging