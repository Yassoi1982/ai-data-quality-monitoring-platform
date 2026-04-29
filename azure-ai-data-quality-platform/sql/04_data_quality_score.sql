WITH metrics AS (
    SELECT
        COUNT(*) AS total_rows,
        SUM(CASE WHEN Amount IS NULL OR Class IS NULL OR Time IS NULL THEN 1 ELSE 0 END) AS null_rows,
        COUNT(*) - COUNT(DISTINCT CONCAT(Time, '-', Amount, '-', Class)) AS duplicate_rows,
        SUM(CASE WHEN Amount < 0 THEN 1 ELSE 0 END) AS invalid_amount_rows
    FROM creditcard_transactions
)
SELECT
    total_rows,
    null_rows,
    duplicate_rows,
    invalid_amount_rows,
    ROUND(
        100
        - ((null_rows * 100.0) / total_rows)
        - ((duplicate_rows * 100.0) / total_rows)
        - ((invalid_amount_rows * 100.0) / total_rows),
        2
    ) AS data_quality_score
FROM metrics;