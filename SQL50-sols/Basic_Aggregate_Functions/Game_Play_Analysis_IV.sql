# Write your MySQL query statement below
SELECT 
    ROUND(COUNT(DISTINCT a1.player_id)
        / (SELECT
            COUNT(DISTINCT a2.player_id)
        FROM
            Activity a2)
    , 2) AS fraction
FROM
    Activity a1
WHERE 
    (a1.player_id, DATE_SUB(a1.event_date, INTERVAL 1 DAY)) IN (
        SELECT
            a3.player_id, MIN(a3.event_date)
        FROM
            Activity a3
        GROUP BY
            a3.player_id 
    );