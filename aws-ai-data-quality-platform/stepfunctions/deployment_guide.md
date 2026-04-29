# Step Functions Deployment Guide

## Steps

1. Go to AWS Step Functions
2. Create state machine
3. Choose "Write workflow in code"
4. Paste JSON from:
{
  "bucket": "ai-data-quality-bucket-yassoi",
  "key": "creditcard.csv",
  "threshold": 90
}