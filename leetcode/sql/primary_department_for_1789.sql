--https://leetcode.com/problems/primary-department-for-each-employee/description/?envType=study-plan-v2&envId=top-sql-50
# Write your MySQL query statement below
SELECt employee_id, department_id FROM Employee
GROUP BY employee_id
HAVING COUNT(employee_id) = 1
UNION
SELECT employee_id, department_id  FROM Employee
WHERE primary_flag = "Y"