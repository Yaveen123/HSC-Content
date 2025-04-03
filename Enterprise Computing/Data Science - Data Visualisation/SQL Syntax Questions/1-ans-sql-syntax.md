For each question, write the SQL query that would retrieve the requested information based on the following hypothetical database schema:


**Customers Table:**

| Column Name | Data Type |
| ----------- | --------- |
| CustomerID  |INT (Primary Key) |
| FirstName	  | VARCHAR(50) |
| LastName    | VARCHAR(50) |
| City        | VARCHAR(50) |
| Email	      | VARCHAR(100) |

**Orders Table:**

| Column Name | Data Type |
| ----------- | --------- |
| OrderID     | INT (Primary Key) |
| CustomerID  | INT (Foreign Key referencing Customers) |
| OrderDate   | DATE  |
| TotalAmount | DECIMAL(10, 2) |
| OrderStatus | VARCHAR(20) |


Questions:

1. Write a query to retrieve the FirstName and LastName of all customers.
> SELECT FirstName, LastName 
> FROM Customers ;

2. Write a query to retrieve all columns from the Orders table.
> SELECT *
> FROM Orders;

3. Write a query to find all customers who live in the city of 'London'.
> SELECT *
> FROM Customers
> WHERE City = 'London';

4. Write a query to find all orders with a TotalAmount greater than 100.00.
> SELECT *
> FROM Orders
> WHERE TotalAmount > 100.00;

5. Write a query to find all orders placed on the date '2025-04-05'.
> SELECT *
> FROM Orders
> WHERE OrderDate = '2025-04-05';

6. Write a query to find customers whose LastName starts with the letter 'S'.
> SELECT *
> FROM Customers
> WHERE LastName LIKE 'S%';

7. Write a query to find orders with an OrderStatus of either 'Pending' or 'Shipped'.
> SELECT *
> FROM Orders
> WHERE OrderStatus IN ('Pending', 'Shipped');

8. Write a query to retrieve the OrderID and OrderDate of all orders, ordered by OrderDate in ascending order.
> SELECT OrderID, OrderDate
> FROM Orders
> ORDER BY OrderDate ASC;

9. Write a query to retrieve the FirstName and City of all customers, ordered by City in descending order.
> SELECT FirstName, City
> FROM Customers
> ORDER BY City DESC;

10. Write a query to find all orders placed between '2025-04-01' and '2025-04-10' (inclusive).
> SELECT *
> FROM Orders
> WHERE OrderDate BETWEEN '2025-04-01' AND '2025-04-10';

11. Write a query to find customers who do not have an email address listed (i.e., Email is NULL).
> SELECT *
> FROM Customers
> WHERE Email IS NULL;

12. Write a query to retrieve the CustomerID, OrderDate, and TotalAmount of all orders with a TotalAmount less than or equal to 50.00, ordered by TotalAmount in descending order.
> SELECT CustomerID, OrderDate, TotalAmount
> FROM Orders
> WHERE TotalAmount <= 50
> ORDER BY TotalAmount DESC;

