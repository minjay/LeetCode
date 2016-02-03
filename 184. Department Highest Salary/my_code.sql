# Write your MySQL query statement below
select Department, Employee, Salary
from (select D.Name as Department, E.Name as Employee, E.Salary, (
        select count(distinct E2.Salary)
        from Employee E2 join Department D2 on
        E2.DepartmentId=D2.Id
        where E.Salary<=E2.Salary and D.Id=D2.Id) as Rank
    from Employee E join Department D on
    E.DepartmentId=D.Id) C
where Rank=1

-- Another Sol
# Write your MySQL query statement below
select Department.Name, Employee.Name, Salary
from Employee join Department on Employee.DepartmentId = Department.Id
where Employee.Salary = (
    select max(Salary) 
    from Employee E2 
    where E2.DepartmentId=Department.Id);