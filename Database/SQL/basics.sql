show databases;
-- create database upflairs;
USE  world; 
SHOW tables;
select * from city;
select ID, Name, District from city;
use upflairs;
show tables;
create table studentdata (student_id INT , student_name VARCHAR(30) , student_rollno INT , student_branch VARCHAR(30), student_city varchar(35));
select * from studentdata;
desc studentdata;
ALTER TABLE studentdata ADD college_city VARCHAR(30);

-- distinguish between drop , truncate and delete
-- normalization and denormalization
-- schema , RDBMS and DBMS and there difference
-- SQL vs NoSQL

DROP TABLE studentdata; -- deletes the entire table including rows and columns
SHOW  tables; 

INSERT INTO studentdata ( student_id, student_name, student_rollno, student_branch , student_city, college_city) 
VALUES (01 , "Manish", 101, "CSE", "Pali", "Jaipur");
INSERT INTO studentdata VALUES 
(2, 'Anshika', 102, 'IT', 'Kota', 'Kota'),
(3, 'Rohit', 103, 'CS', 'Delhi', 'Delhi'),
(4, 'Priya', 104, 'ECE', 'Mumbai', 'Mumbai'),
(5, 'Amit', 105, 'ME', 'Bangalore', 'Bangalore'),
(6, 'Sneha', 106, 'EE', 'Jaipur', 'Jaipur'),
(7 , "Harsh", 107, "ECE", "Pune", "Jaipur");

SELECT * FROM studentdata;
SELECT * FROM studentdata WHERE student_city = "jaipur";

TRUNCATE TABLE studentdata; -- deletes all records of the table excluding rows and columns

SET SQL_SAFE_UPDATES = 0; -- (0) --> False - TO get out of safe update mode
DELETE FROM studentdata WHERE student_name = "Akshay"; -- deletes specific defined record

-- select * from shippings where status != 'Pending';
-- select * from shippings where status != 'Pending';
-- select * from shippings where status <> 'Pending';
-- select * from shippings where not status = 'Pending';

-- select * from customers where age >= 22 and age<= 25;
-- select * from customers where age between 22 and 25;

-- Union --> unique elements are filter and are united
-- select * from customers
-- union
-- select * from customers

-- Union All --> unique and duplicate elements are united
-- select * from customers
-- union all
-- select * from customers

-- no. of columns entered should be same at both sides
-- select first_name from customers
-- union
-- select first_name, last_name from customers

-- select first_name, age from customers
-- union
-- select age, first_name from customers

SET SQL_SAFE_UPDATES = 0;
UPDATE studentdata SET student_name = "Radhey" WHERE student_rollno = 101;
UPDATE studentdata SET student_city = "Delhi" WHERE student_branch = "CS";
SELECT * FROM studentdata;






























