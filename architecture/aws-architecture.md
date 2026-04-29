# AWS Architecture Diagram

```text
User Upload CSV → S3 Bucket
                     ↓
             Lambda (Validate Data)
                     ↓
             Lambda (Anomaly Detection)
                     ↓
             Lambda (Send Alert)
                     ↓
                 SNS Email Alert
                     ↓
           Step Functions Orchestration