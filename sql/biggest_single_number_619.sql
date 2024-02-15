--https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50
# Write your MySQL query statement below
SELECT
    MAX(num) AS num
FROM (SELECT num FROM MyNumbers
GROUP BY num
HAVING COUNT(*) = 1
) AS max_table;
