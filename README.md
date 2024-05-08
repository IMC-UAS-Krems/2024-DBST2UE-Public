# Public repository for DBST2UE 2024

## Session 9 - 08/05/2024

### Task 1.1: More Queries

Given the following SQL Schema:

```
CREATE TABLE Person (
	name VARCHAR(255),
	age UNSIGNED INT NOT NULL CHECK (age > 0 AND age < 130),
	gender CHAR CHECK (gender IN ("M", "F", "O", "m", "f", "o")),
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

1. Find all pizzerias that are frequented by only `female`s or only `male`s.

2. For each person, find all pizzas the person eats that are not served by any pizzeria the person frequents. Return all such person name and pizza pairs.

3. Find the names of all people who frequent only pizzerias serving at least one pizza they eat.

4. Find the names of all people who frequent every pizzeria serving at least one pizza they eat.

5. Find the pizzeria serving the cheapest pepperoni pizza. In the case of ties, return all of the cheapest-pepperoni pizzerias.

### Task 1.2: Views

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

1. Create a View on top of `Employee`, accessing only the attributes `id` and `name` of "Developers"

2. Try to insert and update values in that view. How does the table change?

3. Create another View that shows the name of "overcrowded" departments, i.e., departments that have more than 3 Employees.

### Task 1.3 Dealing with References
Update the Employee table and add an update and delete clause  on the foreign key. Make sure they are different.

1. Which update/delete clause did you choose?
2. Discuss how the update delete clauses affect the Employee table after updating and deleting the related entries in Department.
3. Execute the update and check that the table was modified as expected. Next, execute the delete and check that table was modified as expected

### Task 2: SQL Alchemy
Implement the database in Python using SQL Alchemy, fill it with input data, and run some the queries from Task 1.

Implement the queries as test cases (one test, one query) and run the tests against a local SQLIte and a "dockerized" MariaDB using the test fixtures that you implemented during the Self-Learning activities 

## Log of Past Sessions

### Session 1 - 06/03/2024

We started the setup of students environment to get ready for the assignment and the exercises in class.

We configured PowerShell/Shell, created an ssh key (in the default location), registered the ssh key into GitHub. 

We checked the installation of `git` and `python`. For the moment we do not enforce any specific version of python.

We accepted the Classroom assignment for DBST2UE and added this repository as git submodule under the name `public`. We committed the changes and pushed back, checked on GitHub that the public folder is actually a link to another repository (e.g., this repository at the time we add the submodule).

We created a python virtual environment called `.venv` in the student repository (besides the `public` folder). Activated the virtual environment, updated `pip`, and installed testing dependencies including `pytest`, `pytest-cov`, and `pytest-mock`. 

Finally, we smoke-tested `pytest` by running it at the root of the probject.

The student repository at this point MUST look like this:

```
.
├── .git
├── .github
├── .gitmodules
├── .venv
├── README.md
└── public
    ├── .git
    ├── .gitignore
    └── README.md
```



### Session 2 - 13/03/2024

We finished to setup the python project, including importing the right submodule, installing pytest, pytest-cov, etc in the virtualenv `.venv`

Dr. Gambi illustrated how to configure and invoke the `pytest-cov` plugin, filter out empty files, test files, and all the files that do not belong to the project. We also included the `__init__.py` files that identify python modules.

We postponed tasks 3 to 5 to Session 3

### Session 3 - 20/03/2024

We finished to install all the dependencies, such as SQLite3 and docker. 

We experimented using docker and docker compose using MariaDB container and instructions. We experimented on how to start a plain container with environmental variables, how to connect to it using `docker exec`, and how to connect to it using port forwarding

We introduced to concept of test fixture, experimented with hardcoded and temporary files to illustrate the problem of state polluting tests.

### Session 4 - 03/04/2024

We completed the missing tasks the previous session.03 and exercised a bit on mapping a database descriptions in natural languages into ER-Models. We identify entities and relationships, discussed where to put attributes, and how to set cardinalities/participations. In one case, we also relied on Generalization (is-a) from EER.

The database model we designed implemented the backend of a simple music collection system and the description was inspired by content available at [O'Reilly Learning My SQL](https://www.oreilly.com/library/view/learning-mysql/0596008643/ch04s04.html) and [Geeks For Geeks](https://www.geeksforgeeks.org/how-to-design-a-database-for-music-streaming-app/)

### Session 5 - 10/04/2024

We reverse engineered an ER model from the pizza RM. We discussed alternative design choices at the ER-level and checked whether these could be mapped correctly back to RM-level. 

We also argued about possible simplifications considering entities with only the key attribute, weak entities, and entities connected  by 1:N relationships.

We skipped Task 2 on generating data and implementing the RM into SQLite.

We wrote two queries in Relational Algebra, a simple one, and the second that made use of set operators. We solved the queries by splitting complex queries into simpler ones.

### Session 6 - 18/04/2024

Self-Learning - Part 1

### Session 7 - 23/04/2024

Self-Learning - Part 2

### Session 8 - 24/04/2024

We exercise some more with RA on the pizza database and we started working with SQL to create tables and define constraints (SQL as DDL). Additionally, we also started to insert data/values in the database (SQL as DML).
