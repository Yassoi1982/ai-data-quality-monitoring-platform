# Lambda Layer Guide

Use a Lambda layer for shared Python dependencies such as pandas and scikit-learn.

## Dependencies

- pandas
- scikit-learn
- numpy

## Packaging idea

Install dependencies into a layer package, zip it, upload it as a Lambda Layer, then attach the layer to all Lambda functions.