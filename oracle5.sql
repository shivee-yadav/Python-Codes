select * from tab--for all tables

select last_name,hire_date
from employees
where last_name like 'G%';

select sysdate from dual;

select last_name,(sysdate-hire_date)/7 as weeks
from employees
where DEPARTMENT_ID=90;--gives no. of weeks from hire date till current date

select last_name,(sysdate-hire_date)/365 as years
from employees
where DEPARTMENT_ID=90;--gives no. of years from hire date till current date

select last_name,MONTHS_BETWEEN(sysdate ,hire_date)
from employees

select add_MONTHS(sysdate ,2)--adding months
from dual

select next_day(sysdate,'thursday') from dual--day from that date

select last_day(sysdate) from dual;
--sysdate=29-04-22
select round(sysdate,'month') from dual;--->01-05-2022
select round(sysdate,'year') from dual;--->01-01-2022
select trunc(sysdate,'month') from dual;--->01-04-2022
select trunc(sysdate,'year') from dual;--->01-01-2022

select to_char(sysdate,'dd-mm-yy') from dual;
select to_char(sysdate,'yyyy') from dual;
select to_char(sysdate,'dd-mm-yy') from dual;
select to_char(sysdate,'year') from dual;
select to_char(sysdate,'dd-mon-yy') from dual;
select last_name,to_char(hire_date,'dd-mon-yyyy')
from employees

describe EMPLOYEES

