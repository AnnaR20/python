use shop1;
create table logs (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT "Идентификатор строки",
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Время создания строки",
    table_name VARCHAR(100) not null,
    id_from_table INT UNSIGNED NOT null,
    name_from_table VARCHAR(100) not null
) ENGINE=Archive;

delimiter //

create trigger users_insert_row after insert on users
for each row
begin 
	insert into logs (created_at, table_name, id_from_table, name_from_table) values (
	NOW(),
	'users',
	new.id,
	new.name
	);
end//

create trigger catalogs_insert_row after insert on catalogs
for each row
begin 
	insert into logs (created_at, table_name, id_from_table, name_from_table) values (
	NOW(),
	'catalogs',
	new.id,
	new.name
	);
end//

create trigger products_insert_row after insert on products
for each row
begin 
	insert into logs (created_at, table_name, id_from_table, name_from_table) values (
	NOW(),
	'products',
	new.id,
	new.name
	);
end//

delimiter ;

insert into users (name, birthday_at) values ('Леонид', '1978-11-23');
select * from users;
select * from logs;




