# Write your MySQL query statement below
delete from Person
where Id in (
    select P1.Id
    from (select * from Person) P1, (select * from Person) P2
    where P1.Id>P2.Id and P1.Email=P2.Email);