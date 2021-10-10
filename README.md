# SQL_generator

Generate SQL create and insert sql commands from config textual files.

The config files in resources folder are the config format.
The existing col_properties config produces the below insert statement

```
INSERT INTO tableA ( col1_id, col2, col3_name, col4, col5, col6 ) values 
 ( 50,88,'A M X','CC','BBE','18-04-2021 16:23:32' ),
 ( 51,95,'A M Y','BB','BBE','28-04-2021 09:43:25' ),
 ( 52,82,'A M Z','BB','CCE','24-04-2021 16:40:27' ),
 ( 53,89,'A N X','BB','CCE','02-05-2021 16:21:37' ),
 ( 54,71,'A N Y','AA','CCE','20-04-2021 17:50:04' );
 ```
 
 The existing ddl_text config produces the below create table statement
 
 ```
CREATE TABLE Employee (
ID int PRIMARY KEY,
name varchar(100) ,
office_number int ,
floor_number int ,
phone_number int ,
email_address varchar(100)  );
 ```
