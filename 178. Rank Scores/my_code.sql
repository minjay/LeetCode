# Write your MySQL query statement below
select S1.Score, (
    select count(distinct S2.Score)
    from Scores S2
    where S1.Score<=S2.Score) as Rank
from Scores S1
order by S1.Score desc;