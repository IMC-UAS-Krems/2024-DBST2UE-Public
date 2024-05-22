# Public repository for DBST2UE 2024

## Session 11 - 22/05/24

### Task 1 Normalization

Given the following table:

|StudID |CourseID |StudName |CourseName |Grade| FacName |FacPhone|
|-----|-----|-----|-----|-----|-----|-----|
1 | PROG2, DBSE2UE | Adams | Prog2, Database | 1, 2 | Dhungana, Gambi | 1234, 1122
2 | PROG2 | Jones | Prog2 | 3  | Dhungana | 1234
3 | PROG2 | Smith | Prog2 | 1  | Dhungana | 1234
4 | PROG2, DBSE2UE| Baker | Prog2, Database | 3, 1 | Dhungana, Gambi| 1234, 1122

#### Task 1.1

The above table is susceptible to update anomalies. Provide examples of insertion, deletion, and modification anomalies.

#### Task 1.2
Given the following functional dependencies

- StudID → StudName
- StudID, CourseID → Grade
- CourseID → CourseName
- CourseID → FacName
- FacName → FacPhone

Check if they hold in the above table.

#### Task 1.3

Describe and illustrate the process of normalizing the table shown to 3NF. For each of the steps below list the relations and their Primary Keys

1. 1NF
2. 2NF
3. 3NF 

### Task 2. Transaction

A schedule is an ordering of operations belonging to different transactions. 

A schedule is **serializable** if it is equivalent to a **serial** schedule, which executes all the operations comprising a query before executing the operations that belong to the next query.

Check whether the following schedules are serializable. Explain your answer.

> Note: `READ (A, t)` stands for reading the value of `A` from the DB into the value of variable `t`, whereas `WRITE (A, t)` stands for storing the value of variable `t` into the database as `A`.

### Schedule 1
| T1 | T2 |
|----|----|
|READ (A, t) | | 
| t := t + 100 | |
| WRITE (A, t) | |
| | READ (A, s)| 
| | s := s * 2 |
| | WRITE (A, s) |
| | READ (B, s) |
| | s := s * 2 |
| | WRITE (B, s) |
| READ (B, t) | |
| t := t + 100 | |
| WRITE (B, t) | |

### Schedule 2
| T1 | T2 |
|----|----|
|READ (A, t) | | 
| t := t + 100 | |
| WRITE (A, t) | |
| | READ (A, s)| 
| | s := s * 2 |
| | WRITE (A, s) |
| READ (B, t) | |
| t := t + 100 | |
| WRITE (B, t) | |
| | READ (B, s) |
| | s := s * 2 |
| | WRITE (B, s) |


## Session 12 - 29/05/24
### Task 1: Deadlocks

Given the following schedule:

| Tr  | 1     | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
|-----|-------|------|------|------|------|------|------|------|------|
| 1   | S(A)  | S(D) |      | S(B) |      |      |      |      |      |
| 2   |       |      | X(B) |      |      |      | X(C) |      |      |
| 3   |       |      |      |      | S(D) | S(C) |      |      | X(A) |
| 4   |       |      |      |      |      |      |      | X(B) |      | 

#### Task 1.1 
Check if the schedule leads to a deadlock when all the locks are exclusive 

#### Task 1.2
Check if the situation changes if we can distinguish between shared and exclusive locks.


> Note: The following table shows the lock compatibility of Shared (S) and Exclusive (X) locks:


|   | **S** | **X** |
|---|---|---|
| **S** | OK | – |
| **X** | – | – |


## Log of Past Sessions

### Session 1 - 06/03/2024

We started the setup of the students' environment to get ready for the assignment and the exercises in class.

We configured PowerShell/Shell, created an SSH key (in the default location), and registered the SSH key on GitHub. 

We checked the installation of `git` and `python`. We do not enforce any specific version of Python at the moment.

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

### Session 9 - 08/05/2024

We exercise more on complex SQL queries that requires the use of set operators, nested queries and subqueries. We used the Pizza db as test subject. We discussed conceptual approaches to generate test cases to validate our queries.
We experimented creating and modifying views.
We discussed the implications of different configurations of the referential constraint triggers (ON DELETE|ON UPDATE).

### Session 10 - 06/03/2024

We exercise on translating SQL queries CANONICAL query trees, estimating their cost, and optimizing them by restructuring the query trees.

We had an hands on experience on:

- installing packages into a linux docker container
- connecting to a mariadb database running inside docker
- installing/creating a mariadb from a database dump stored in a `.sql` file
- Creating index on non-key attributes, observing the performance speedup, and using EXPLAIN/ANALYZE to gather more info on the query
