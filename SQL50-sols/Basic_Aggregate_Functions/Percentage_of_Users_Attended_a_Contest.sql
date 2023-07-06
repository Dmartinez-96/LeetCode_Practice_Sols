# Write your MySQL query statement below
SELECT r.contest_id, ROUND(100 * COUNT(distinct(r.user_id)) / COUNT(distinct(u.user_id)), 2) AS percentage
FROM Register r, Users u
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;