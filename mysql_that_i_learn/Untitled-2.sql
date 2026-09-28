use sql_invoicing;
select max(invoice_total) as highest,
min(invoice_total)as lowest ,
avg(invoice_total)as average,
sum(invoice_total*1.1) as total,

count(distinct client_id) as total_records
from invoices
where invoice_date >'2019-07-01';


-- to use distinct to reduce the continuous values

select 
'First half of 2019' as date_range,
sum(invoice_total) as total_sales,
sum(payment_total) as total_payments,
sum(invoice_total-payment_total) as what_we_expect
from invoices 
where invoice_date
between '2019-01-01'and '2019-06-30'
union 
select 
'Second half of 2019' as date_range,
sum(invoice_total) as total_sales,
sum(payment_total) as total_payments,
sum(invoice_total-payment_total) as what_we_expect
from invoices 
where invoice_date
between '2019-06-30'and '2019-12-30'
union 
select 
'Total' as date_range,
sum(invoice_total) as total_sales,
sum(payment_total) as total_payments,
sum(invoice_total-payment_total) as what_we_expect
from invoices 
where invoice_date
between '2019-01-01'and '2019-12-30';

-- how to use group by ?
select 
state,city,
sum(invoice_total)as total_sales
from invoices i    
join clients using (client_id)

group by state,city;



SELECT 
date ,
pm.name as payment_method,
sum(amount) as total_payment
from payments p  
join payment_methods pm 
on p.payment_method =pm.payment_method_id

group by date,payment_method
order by  date ;

-- 我有些搞不懂为什么这个group要搞两个


select 
client_id,
sum(invoice_total) as total_sales ,
count(*) as number_of_invoices
from invoices
-- where total_sales>500  不可行    用where可以用任何列 不管我们是否选择了它
group by  client_id
-- 使用 having在行分组后筛选数据
having total_sales>500 and number_of_invoices >5;
-- 但是having这里用带的列 一定得是我们select子句中存在的




-- rollup 只能运用于聚合值的序列,只适用于MySQL，不是标准的sql语言,
select 
state,city,
sum(invoice_total) as total_sales
from invoices i    
join clients c  using (client_id)
group by state,city with rollup;





-- 练习
use sql_invoicing;
select
 pm.name as payment_method,
sum(amount) as total
from payments p
join payment_methods pm
on p.payment_id =pm.payment_method_id

group by  pm.name with rollup;

-- g b 里面不能用别名


use sql_store;
select 
c.customer_id,
c.first_name,
c.last_name,
sum(oi.quantity *oi.unit_price) as total_sales
from customers c

join orders o
using(customer_id)
join order_items oi 
using(order_id)

where c.state ='VA'
group by c.customer_id,
c.first_name,
c.last_name
having total_sales>100;













