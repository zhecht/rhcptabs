
drop table if exists Songs;
CREATE TABLE Songs
(
s_id int NOT NULL AUTO_INCREMENT,
album varchar(75),
title varchar(75),
total int,
PRIMARY KEY (s_id)
);