# Write your MySQL query statement below
SELECT emp.name
FROM Employee e
INNER JOIN Employee emp
WHERE e.managerID = emp.id
GROUP BY e.managerID HAVING COUNT(*) >= 5;