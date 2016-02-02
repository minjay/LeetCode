# Write your MySQL query statement below
select DName, EName, Salary
from (
    select D.Name as DName, E.Name as EName, E.Salary, (
        select count(distinct E2.Salary)
        from Employee E2 join Department D2 on
        E2.DepartmentId=D2.Id
        where E.Salary<=E2.Salary and D.Id=D2.Id) as RANK
    from Employee E join Department D on
    E.DepartmentId=D.Id) C
where RANK<=3;