-- https://leetcode.com/problems/find-total-time-spent-by-each-employee/submissions/
-- Total Time Spent by Each Employee 
--  Group By, Sum function

SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id 