-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/discuss/53475/A-straightforward-method

-- # Write your MySQL query statement below
SELECT E1.Name AS "Employee"
FROM Employee E1
    JOIN Employee E2
    ON E1.ManagerId = E2.Id
WHERE E1.Salary > E2.Salary


-- Advantages Of Subquery:
-- Complex query can be broken down into a series of logical steps.
-- Subquery is easy to read, understand and maintain.
-- It allow to use the results of another query in the outer query.

-- Disadvantages of Subquery:
-- Execution is slower than JOIN.
-- We cannot modify a table and select from the same table within a subquery in the same SQL statement.

--  Using SubQuery 
SELECT Name as Employee FROM Employee e
WHERE Salary > (
    Select Salary FROM Employee m WHERE m.Id = e.ManagerId
)

-- Advantage of a JOIN
-- Execution and retrieval time faster than subqueries.

-- Disadvantages Of JOIN:
-- Database server has to do more work when it comes to a lot of joins in a query => more time consuming to retrieve data
-- Developer can be confused to choose the appropriate type among many types of joins.
