-- https://leetcode.com/problems/customers-who-never-order/

SELECT Name AS "Customers"
FROM Customers 
    LEFT JOIN Orders 
    ON Customers.Id = Orders.CustomerId

WHERE Orders.CustomerId IS NULL 


-- Other Solutions 
SELECT A.Name from Customers A
WHERE A.Id NOT IN (SELECT B.CustomerId from Orders B)

SELECT A.Name from Customers A
WHERE NOT EXISTS (SELECT 1 FROM Orders B WHERE A.Id = B.CustomerId)