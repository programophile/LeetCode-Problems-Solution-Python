# Write your MySQL query statement below
select s.name from SalesPerson s where s.sales_id NOt in (Select 
o.sales_id 
from Company c join Orders o on c.com_id = o.com_id where c.name="RED")