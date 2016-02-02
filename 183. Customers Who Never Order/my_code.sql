# Write your MySQL query statement below
select Name
from Customers
where Id not in (
    select CustomerID
    from Orders)