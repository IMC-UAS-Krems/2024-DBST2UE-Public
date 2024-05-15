# Session 9 - 08/05/2024

## Task 1.1: More Queries

Given the following SQL Schema:

```
CREATE TABLE Person (
	name VARCHAR(255),
	age UNSIGNED INT NOT NULL CHECK (age > 0 AND age < 130),
	gender CHAR CHECK (gender IN ('M', 'F', 'O', 'm', 'f', 'o')),
	PRIMARY KEY(name)
);

CREATE TABLE Frequents (
	name VARCHAR(255) NOT NULL,
	pizzeria VARCHAR(255) NOT NULL,
	PRIMARY KEY(name, pizzeria),
	FOREIGN KEY (name) REFERENCES Person(name)	
);

CREATE TABLE Eats(
	name VARCHAR(255) NOT NULL,
	pizza VARCHAR(255) NOT NULL,
	PRIMARY KEY(name, pizza),
	FOREIGN KEY (name) REFERENCES Person(name)
);

CREATE TABLE Serves(
	pizzeria VARCHAR(255) NOT NULL,
	pizza VARCHAR(255) NOT NULL,
	price NUMERIC(10,2) NOT NULL CHECK (price > 0),
	PRIMARY KEY(pizzeria, pizza)
);
```

Write the following queries, possibly using set operators, nested queries, views and the like. Whenever possible, argue whether you could have rewritten the queries in a different way (e.g., without nesting, without set operators).

For each query, define a set of tests (inputs) that check it correctness. Typical examples include running the query against:

- an empty db
- a db containing NULL values (when the constraints allow for them)
- a db with (partially) matching tuples (e.g., for testing joins).


Possible queries:

1. Find the pizzeria serving the cheapest pepperoni pizza. In the case of ties, return all of the cheapest-pepperoni pizzerias.
2. Find the names of all people who frequent only pizzerias serving at least one pizza they eat.
3. Find the names of all people who frequent every pizzeria serving at least one pizza they eat.



## Task 1.2: Views

Given the following SQL Schema:

```
CREATE TABLE Department(id INTEGER PRIMARY KEY, name TEXT);

CREATE TABLE Employee(id INTEGER PRIMARY KEY, name TEXT, role TEXT, dep_id INTEGER, FOREIGN KEY (dep_id) REFERENCES Department(id)) ;
```

Filled with the data:

```
INSERT INTO Department(id, name) VALUES(1, 'Accounting');
INSERT INTO Department(id, name) VALUES(2, 'IT');


INSERT INTO Employee(name, role, dep_id) VALUES('John Doe', 'Manager', 2);
INSERT INTO Employee(name, role, dep_id) VALUES('Jane Smith', 'Developer', 2);
INSERT INTO Employee(name, role, dep_id) VALUES('David Gray', 'Developer', 2);
INSERT INTO Employee(name, role, dep_id) VALUES('Mia Brown', 'Sales', 1);
INSERT INTO Employee(name, role, dep_id) VALUES('Max Green', 'Developer', 2);
```

1. Create a View on top of `Employee`, accessing only the attributes `id` and `name` of 'Developers'

2. Try to insert and update values in that view. How does the table change?

3. Create another View that shows the name of 'overcrowded' departments, i.e., departments that have more than 3 Employees.

## Task 1.3 Dealing with References
Update the Employee table and add an update and delete clause  on the foreign key. Make sure they are different.

1. Which update/delete clause did you choose?
2. Discuss how the update delete clauses affect the Employee table after updating and deleting the related entries in Department.
3. Execute the update and check that the table was modified as expected. Next, execute the delete and check that table was modified as expected

## Task 2: SQL Alchemy
Implement the database in Python using SQL Alchemy, fill it with input data, and run some the queries from Task 1.

Implement the queries as test cases (one test, one query) and run the tests against a local SQLIte and a 'dockerized' MariaDB using the test fixtures that you implemented during the Self-Learning activities 
