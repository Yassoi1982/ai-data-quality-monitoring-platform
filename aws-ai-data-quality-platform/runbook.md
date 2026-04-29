# AWS Pipeline Runbook

## Goal
Execute the full AI Data Quality Monitoring pipeline.

## Steps

1. Upload dataset to S3
   - Bucket: ai-data-quality-bucket-yassoi
   - File: creditcard.csv

2. Test Lambda (Validate Data)
   - Input:
```json
{
  "bucket": "ai-data-quality-bucket-yassoi",
  "key": "creditcard.csv",
  "threshold": 90
}