SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN Time IS NULL THEN 1 ELSE 0 END) AS null_time,
    SUM(CASE WHEN Amount IS NULL THEN 1 ELSE 0 END) AS null_amount,
    SUM(CASE WHEN Class IS NULL THEN 1 ELSE 0 END) AS null_class
FROM creditcard_transactions;