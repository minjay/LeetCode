CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary
      from (
        select E1.Salary, (
            select count(distinct E2.Salary)
            from Employee E2
            where E1.Salary<=E2.Salary) as Rank
        from Employee E1) C
      where Rank=N
  );
END