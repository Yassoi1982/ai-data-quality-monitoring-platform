# GCP IAM Guide

## Purpose
Configure permissions for Cloud Functions to access Cloud Storage and other services.

## Required Roles

- Storage Object Viewer (read CSV from bucket)
- Cloud Functions Invoker
- Logging Writer

## Service Account

1. Go to IAM & Admin → Service Accounts
2. Create new service account
3. Assign roles above
4. Attach to Cloud Functions

## Principle

Use least privilege access for production environments.