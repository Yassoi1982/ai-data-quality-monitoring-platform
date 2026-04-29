# Azure Architecture

```text
User uploads creditcard.csv
        ↓
Azure Blob Storage
        ↓
Azure Function: Validate Data
        ↓
Azure Function: Detect Anomalies
        ↓
Azure Function: Send Alert
        ↓
Logic Apps / Azure Monitor