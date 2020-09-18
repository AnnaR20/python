create database shop;
show tables;

-- #1

desc users;
select * from users;
update users set created_at = now(), updated_at = now();

-- #2
-- создадим что были данные VARCHAR
alter table users modify column created_at VARCHAR(255);
update users set created_at = '20.10.2017 8:10';
alter table users modify column updated_at VARCHAR(255);
update users set updated_at = '20.10.2017 8:10';
-- преобразование к DATETIME
update users set created_at = STR_TO_DATE(created_at, '%d.%m.%Y %h:%i');
alter table users modify column created_at DATETIME;
update users set updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %h:%i');
alter table users modify column updated_at DATETIME;

-- #3
desc storehouses_products;
select * from storehouses_products;
-- заполняем таблицу данными
insert into storehouses_products (storehouse_id, product_id, value) values
  (53, 326, 0),
  (23, 456, 2500),
  (53, 677, 0),
  (12, 435, 30),
  (53, 688, 500),
  (21, 459, 1);
-- сортируем
select * from storehouses_products order by value = 0, value;

-- #4
select monthname(birthday_at), name from users where monthname(birthday_at) = 'May' or monthname(birthday_at) = 'August';

-- Тема Агрегация данных
-- #1
select round(avg(to_days(NOW()) - to_days(birthday_at))/365.25, 2) as avg_age from users;

-- #2
select count(*), dayname(STR_TO_DATE(date_format(birthday_at, '2020-%m-%d'), '%Y-%m-%d')) as week_day from users group by week_day order by count(*) desc;

