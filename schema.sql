drop table if exists entries;
create table entries(
	id int primary key autoincrement,
	title text not null,
	text text not null
	);