-- https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
SELECT
        p.project_id,
        ROUND(SUM(e.experience_years)/COUNT(e.experience_years),2) as average_years
FROM
        project p
LEFT JOIN employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;