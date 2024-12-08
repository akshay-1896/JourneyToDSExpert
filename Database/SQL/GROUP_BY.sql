CREATE DATABASE groupby;
USE groupby;
SHOW TABLES;

-- Create the Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Department VARCHAR(50),
    Salary INT
);

DROP TABLE EMPLOYEES;
-- Insert 15 records into the Employees table
INSERT INTO Employees (EmployeeID, EmpName, Department, Salary)
VALUES
(1, 'Alice', 'HR', 50000),
(2, 'Bob', 'IT', 60000),
(3, 'Carol', 'HR', 55000),
(4, 'David', 'Finance', 70000),
(5, 'Eve', 'IT', 65000),
(6, 'Frank', 'Finance', 72000),
(7, 'Grace', 'HR', 52000),
(8, 'Hank', 'IT', 67000),
(9, 'Ivy', 'Marketing', 58000),
(10, 'Jack', 'Marketing', 60000),
(11, 'Kathy', 'Finance', 75000),
(12, 'Liam', 'IT', 63000),
(13, 'Mona', 'HR', 54000),
(14, 'Nancy', 'Marketing', 62000),
(15, 'Oscar', 'Finance', 80000);

SELECT * FROM EMPLOYEES;

SELECT EmpName, max(Salary) as max_salary
FROM employees
WHERE Department = 'HR'
group by EmpName
order by max_salary desc;

SELECT DEPARTMENT, MAX(SALARY) AS MAXSALARY FROM employees
group by department
ORDER BY MAXSALARY ASC
LIMIT 2 
OFFSET 2; -- To skip the specified initial rows

SELECT DEPARTMENT, avg(SALARY) AS AVGSALARY FROM employees
group by department
ORDER BY AVGSALARY ASC;

SELECT DEPARTMENT, avg(SALARY) AS AVGSALARY FROM employees
group by department
having AVGSALARY > 60000;

SELECT DEPARTMENT, MIN(SALARY) AS MINSALARY FROM employees
group by department HAVING MINSALARY > 50000;

select distinct EmpName, department from employees;

select count(*) from employees where department = "HR" or department = "IT";
select count(*) from employees where department in ("HR","IT");

select * from employees where department not in ("HR","IT");

-- What is index, view and procedure in sql?
-- What are window functions in sql?
-- How we can write subquery in sql?
-- What is CTE in sql?
-- What is like keyword?

-- ORDER OF EXECUTION --

-- from -> join -> where -> group by -> having -> select -> distinct -> order by -> limit -> offset
















