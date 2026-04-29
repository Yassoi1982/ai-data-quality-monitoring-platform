# AWS AI Data Quality Monitoring Platform

## Overview

This module implements a cloud-based data quality monitoring pipeline using AWS services.

It extends the local Python data quality engine to a fully automated, serverless architecture.

---

## Architecture

```text
Amazon S3 (Data Source)
        ↓
Lambda: Validate Data Quality
        ↓
Lambda: Detect Anomalies (ML)
        ↓
Lambda: Send Alert (SNS)
        ↓
AWS Step Functions (Orchestration)