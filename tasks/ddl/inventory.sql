create table if not exists inventory (
	station_id char(11) primary key not null,
	latitude numeric not null,
	longtitude numeric not null,
	element char(4) not null,
	begin_year integer,
	end_year integer);