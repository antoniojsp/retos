--https://leetcode.com/problems/triangle-judgement/description/?envType=study-plan-v2&envId=top-sql-50
# Write your MySQL query statement below
SELECT
    *,
    IF(x + y > z AND x + z > y AND y + z > x, "Yes", "No") as Triangle
FROM triangle
