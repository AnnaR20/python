-- ДЗ 7
-- #1
create database shop1;
insert into orders (user_id) values
     (1),
     (1),
     (6),
     (3),
     (2);
-- 1a
select name from users where id in (select user_id from orders);

-- 1b
alter table orders
    modify column user_id bigint unsigned;
    
alter table orders
    add constraint orders_user_id_fk
      foreign key (user_id) references users(id);

select distinct users.name
    from users join orders
    on users.id = orders.user_id;
   
-- #2
-- 2a
alter table products
    modify column catalog_id bigint unsigned;
  
alter table products
    add constraint products_catalog_id_fk
      foreign key (catalog_id) references catalogs(id);

select p.name, c.name
   from products as p join catalogs as c
   on p.catalog_id = c.id;

-- 2b
  select name,
   (select name from catalogs where id = catalog_id) as 'catalog'
   from products;
   
-- #3
drop table if exists flights;
create table flights (
     id int unsigned AUTO_INCREMENT PRIMARY KEY,
     from_ varchar(100),
     to_ varchar(100));

insert into flights (from_, to_) values
    ('moscow','omsk'),
    ('novgorod','kazan'),
    ('irkutsk','moscow'),
    ('omsk','irkutsk'),
    ('moscow','kazan');

create table cities (
     label varchar(100),
     name varchar(100));

insert into cities (label, name) values
    ('moscow','Москва'),
    ('novgorod','Новгород'),
    ('irkutsk','Иркутск'),
    ('omsk','Омск'),
    ('kazan','Казань');

select (select name from cities where label = from_) as from_, (select name from cities where label = to_) as to_ from flights;
