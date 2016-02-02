# Write your MySQL query statement below
select distinct L1.Num
from Logs L1, Logs L2, Logs L3
where L1.Num=L2.Num and L2.Num=L3.Num and L1.Id=L2.Id-1 and L2.Id=L3.Id-1;