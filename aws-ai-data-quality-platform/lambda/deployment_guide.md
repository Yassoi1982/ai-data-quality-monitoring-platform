# Lambda Deployment Guide

## Steps

1. Create Lambda function in AWS Console
2. Runtime: Python 3.10
3. Upload code as ZIP

## Packaging

Include:
- lambda_function.py
- shared/ folder
- dependencies from requirements.txt

## Install dependencies locally

```bash
pip install -r requirements.txt -t .
zip -r lambda_package.zip .