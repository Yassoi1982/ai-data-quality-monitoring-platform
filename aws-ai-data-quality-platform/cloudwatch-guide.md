# CloudWatch Monitoring Guide

## Purpose
Track execution and debug AWS pipeline.

## Where to check logs

1. AWS Console → CloudWatch
2. Logs → Log Groups
3. Select Lambda function:
   - validate-data-quality
   - detect-data-anomalies
   - send-data-quality-alert

## What to verify

- Execution success
- Errors / exceptions
- Data processing logs

## Tip

Use structured logging in Lambda:

```python
print("Processing started")