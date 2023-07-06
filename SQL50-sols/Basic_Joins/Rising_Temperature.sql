# Write your MySQL query statement below
SELECT W1.id as Id
FROM Weather as W1, Weather as W2
WHERE W2.recordDate = DATE_SUB(W1.recordDate, INTERVAL 1 DAY) AND W1.temperature > W2.temperature;