# Write your MySQL query statement below
SELECT query_name, ROUND(AVG(rating / q.position), 2) as quality,
  ROUND(100 * SUM(rating < 3) / COUNT(query_name), 2) as poor_query_percentage
FROM Queries q
GROUP BY query_name