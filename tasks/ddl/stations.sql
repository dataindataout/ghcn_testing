create table if not exists stations (
	station_id char(11) primary key not null,
	latitude numeric not null,
	longtitude numeric not null,
	elevation numeric not null,
	state_code char(2) null,
	station_name varchar(30) NOT null,
	gsn_flag char(3) null,
	hcn_crn_flag char(3) null,
	wmo_id numeric null);