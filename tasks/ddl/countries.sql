create table if not exists countries (
	country_code char(2) primary key not null,
	country_name varchar(200) not null);