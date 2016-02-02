# Write your MySQL query statement below
select W1.Id
from Weather W1, Weather W2
where datediff(W1.date, W2.date)=1 and W1.Temperature>W2.Temperature;