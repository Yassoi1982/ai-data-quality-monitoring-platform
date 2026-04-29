# Azure Deployment Guide

## Steps

1. Create Azure Storage Account
2. Create Blob container: data-quality-input
3. Upload creditcard.csv
4. Create Azure Function App
5. Deploy validate_data, detect_anomalies, and send_alert functions
6. Configure application settings
7. Test each function with test-events JSON
8. Monitor execution in Azure Monitor