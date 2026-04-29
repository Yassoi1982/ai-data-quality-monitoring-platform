SELECT *
FROM creditcard_transactions
WHERE Amount < 0
   OR Amount > (
        SELECT AVG(Amount) + 3 * STDEV(Amount)
        FROM creditcard_transactions
   );