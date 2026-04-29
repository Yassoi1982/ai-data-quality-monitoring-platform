SELECT
    Time,
    Amount,
    Class,
    COUNT(*) AS duplicate_count
FROM creditcard_transactions
GROUP BY Time, Amount, Class
HAVING COUNT(*) > 1;