--https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below
SELECT
    e2.employee_id,
    e2.name,
    COUNT(e.reports_to) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM employees e
LEFT JOIN employees e2 ON e.reports_to = e2.employee_id
WHERE e.reports_to IS NOT NULL
GROUP BY e.reports_to
ORDER BY employee_id;
