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

2. Write a query to retrieve all columns from the Orders table.

3. Write a query to find all customers who live in the city of 'London'.

4. Write a query to find all orders with a TotalAmount greater than 100.00.

5. Write a query to find all orders placed on the date '2025-04-05'.

6. Write a query to find customers whose LastName starts with the letter 'S'.

7. Write a query to find orders with an OrderStatus of either 'Pending' or 'Shipped'.

8. Write a query to retrieve the OrderID and OrderDate of all orders, ordered by OrderDate in ascending order.

9. Write a query to retrieve the FirstName and City of all customers, ordered by City in descending order.

10. Write a query to find all orders placed between '2025-04-01' and '2025-04-10' (inclusive).

11. Write a query to find customers who do not have an email address listed (i.e., Email is NULL).

12. Write a query to retrieve the CustomerID, OrderDate, and TotalAmount of all orders with a TotalAmount less than or equal to 50.00, ordered by TotalAmount in descending order.
