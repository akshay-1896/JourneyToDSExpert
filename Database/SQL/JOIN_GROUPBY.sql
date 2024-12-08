USE upflairs;
SHOW TABLES;
SELECT * FROM departments;
SELECT * FROM employees;
SELECT * FROM projects;


-- Create the Employees table
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(100),
    DeptID INT
);

-- Insert data into Employees
INSERT INTO Employees (EmpID, EmpName, DeptID) VALUES
(1, 'Alice', 101),
(2, 'Bob', 102),
(3, 'Charlie', 101),
(4, 'Diana', 103),
(5, 'Eve', NULL);

-- Create the Departments table
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(100),
    Manager VARCHAR(100)
);

-- Insert data into Departments
INSERT INTO Departments (DeptID, DeptName, Manager) VALUES
(101, 'Human Resources', 'Karen'),
(102, 'Finance', 'Tom'),
(103, 'Engineering', 'Mike');

-- Create the Projects table
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(100),
    EmpID INT
);

-- Insert data into Projects
INSERT INTO Projects (ProjectID, ProjectName, EmpID) VALUES
(1001, 'Project Alpha', 1),
(1002, 'Project Beta', 2),
(1003, 'Project Gamma', 3),
(1004, 'Project Delta', 4),
(1005, 'Project Epsilon', NULL);

-- INNER JOIN --

SELECT * FROM employees INNER JOIN projects ON employees.EmpID = projects.EmpID;

-- alias --
SELECT * FROM employees as e INNER JOIN projects as p ON e.EmpID = p.EmpID;
-- good practice --
SELECT e.EmpName, p.ProjectName, e.EmpID FROM employees as e INNER JOIN projects as p ON e.EmpID = p.EmpID;


SELECT e.DeptID, e.EmpName, p.ProjectName, e.EmpID FROM employees as e INNER JOIN projects as p ON e.EmpID = p.EmpID 
WHERE 
e.DeptID = 101;

-- If no class is specified, then by default it considers it as INNER Join
SELECT e.DeptID, e.EmpName, p.ProjectName, e.EmpID FROM employees as e JOIN projects as p ON e.EmpID = p.EmpID 
WHERE 
e.DeptID = 101;


-- LEFT JOIN --

SELECT * FROM employees as e LEFT JOIN projects as p ON e.EmpID = p.EmpID ;

-- RIGHT JOIN --

SELECT * FROM employees as e RIGHT JOIN projects as p ON e.EmpID = p.EmpID ;

-- OUTER JOIN --

SELECT * FROM employees FULL JOIN projects;

-- NATURAL JOIN --

SELECT * FROM employees NATURAL JOIN projects; 
-- INNER JOIN which do not requires ON keyword
-- Automatically identifies common column

SELECT * FROM employees NATURAL JOIN departments;

-- By default it applies INNER JOIN if it gets common column
-- But if there does not exists any common column than it applies CROSS JOIN


-- CROSS JOIN --

-- A CROSS JOIN in SQL is a type of join that produces the Cartesian product of two tables. 
-- This means that each row from the first table is paired with every row from the second table, 
-- regardless of whether they are related.
SELECT * FROM departments NATURAL JOIN projects;

DROP TABLE B;
SHOW TABLES;
create table A (test1 int);
create table B (test2 int);

INSERT INTO A (test1) values(1),(2);
INSERT INTO B (test2) values(5),(6),(7);

SELECT * from A CROSS JOIN B;
-- SELECT * FROM A,B; -- short syntax of cross join


-- SELF JOIN --

-- Create the Employees table
CREATE TABLE Emp(
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    ManagerID INT
);

-- Insert records into the Employees table
INSERT INTO Emp (EmpID, Name, ManagerID)
VALUES
(1, 'Alice', NULL),  -- Alice is the top-level manager
(2, 'Bob', 1),       -- Bob reports to Alice
(3, 'Carol', 1),     -- Carol reports to Alice
(4, 'David', 2);     -- David reports to Bob

SELECT * FROM Emp;

SELECT e1.Name, e1.ManagerID, e2.EmpID, e2.Name FROM Emp AS e1 
INNER JOIN Emp as e2 
ON e1.ManagerID = e2.EmpID;

























