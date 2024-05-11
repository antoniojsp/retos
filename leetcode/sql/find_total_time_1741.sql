
#https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/

# Write your MySQL query statement below
SELECT
        event_day as day,
        emp_id,
        ABS(SUM(in_time) - SUM(out_time)) as "total_time"
FROM Employees
GROUP BY emp_id, event_day;