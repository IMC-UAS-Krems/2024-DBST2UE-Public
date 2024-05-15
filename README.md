# Public repository for DBST2UE 2024

## Session 10 - 15/05/24

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

Check if they holds in the above table.

#### Task 1.3

Describe and illustrate the process of normalizing the table shown to 3NF. For each of the steps below list the relations and their Primary Keys

1. 1NF
2. 2NF
3. 3NF 

### Task 2. Query Optimization

Given the following schema:

```
Student(sid, name, age, address)
Book(bid, title, author)
Checkout(sid, bid, date)
```

And assuming:

- There are 10,000 Student records stored on 1,000 pages.
- There are 50,000 Book records stored on 5,000 pages.
- There are 300,000 Checkout records stored on 15,000 pages. 
- There are 500 different authors.
- Student ages range from 7 to 24.

#### Task 2.1:
Show the canonical query execution tree for the following query.


```    
    SELECT S.name
    FROM Student S, Book B, Checkout C
    WHERE S.sid = C.sid
    AND B.bid = C.bid
    AND B.author = 'Olden Fames'
    AND S.age > 12
    AND S.age < 20
```

#### Task 2.2
Suggest an alternative (optimized) query plan for the query of Task 2.1.

#### Task 2.3

Consider the following Relational Model:

```
R(a,b)
S(b,c)
T(b,d)
U(b,e)
```

For the following SQL query, give two equivalent query execution plans such that one is likely to be more efficient than the other. 

```
    SELECT R.a
    FROM R, S
    WHERE R.b = S.b AND
          S.c = 3
```

Indicate which one is likely to be more efficient. Explain.

### Task 3. Hands on 

For this exercise, we need to use an existing database. Among the many sample databases that you find around (e.g., [https://dev.mysql.com/doc/index-other.html](https://dev.mysql.com/doc/index-other.html)) we use the `employee data` a large dataset that includes data and test/verification suite.

The dataset is available also on GitHub:
[https://github.com/datacharmer/test_db](https://github.com/datacharmer/test_db)

#### Setup the DB

Before we can use it with MariaDB, we need to run a new container:

```
docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -p 3306:3306 -d mariadb:10.6
```

Now, we connect to the running container and start the `bash` interpreter:

```
docker exec -it mariadbtest /bin/bash
```

You should see a prompt like this:

```
root@25712fc19ceb:/# 
```

At this point, we can run commands just like regular (Linux/Unix) shell/terminal.

First, we update the local package repository:

```
root@25712fc19ceb:/# apt-get update
```

Next, we install git:

```
root@25712fc19ceb:/# apt-get install git
```

Then, we clone the Employee DB repo from GitHub:

```
root@25712fc19ceb:/# git clone https://github.com/datacharmer/test_db.git
```

We load the database

```
root@25712fc19ceb:/# cd test_db
root@25712fc19ceb:/test_db#: mariadb --user root -pmypass < employees.sql 
```

Next, we test it:

```
root@25712fc19ceb:/test_db# mariadb --user root -pmypass -t < test_employees_md5.sql

```

Finally, we exit from the (bash) container:
```
root@25712fc19ceb:/test_db# exit
```

At this point, we have a (large) database available inside the running docker container and we can connect to it for running queries:

```
docker exec -it mariadbtest mariadb --user root -pmypass
```

>> NOTE: This time we execute the command `mariadb` to start the interpret directly in the container. We could also execute `/bin/bash` and then invoke `mariadb`.

#### Task 3.1

- Using the `EXPLAIN` and `ANALYZE` commands, execute the following query and find out what execution plan is used to run it.

```
SELECT * FROM salaries WHERE salary > 150000;
```
    
- What is the estimated total cost and what the actual total cost of the plan?

- Build an index on the field `salary`. What kind of index was created?

```
CREATE INDEX idx_salary ON salaries(salary);
```

```
SHOW INDEX FROM salaries;
```

- Re-run the query and report its execution plan again.

- What is the estimated total cost and what the actual total cost of the plan now?

- Drop the previously created index

```
ALTER TABLE salaries DROP INDEX idx_salary;
```

#### Task 3.2

- Using the `EXPLAIN` and `ANALYZE` commands, execute the following query and find out the execution plans chosen to run them.

```
  SELECT * FROM employees ORDER BY emp_no;
```
  
```
  SELECT * FROM salaries ORDER BY salary DESC;
```

- What is the estimated total cost and what the actual total cost of the plans?

- Which sorting algorithm was used for each of the queries? Why are they different?

- Build an index for the second query on the field `salary `.

- Re-run the second query and report its execution plan again.

- What is the estimated total cost and what the actual total cost of the plan?

- Check whether the sorting algorithm remained the same or changed after building the index. Explain briefly. 

- Change the second query and report changes in the analysis.

```
SELECT * FROM salaries WHERE salary > 150000 ORDER BY salary;
```

```
SELECT * FROM salaries ORDER BY salary LIMIT 10;
```
```
SELECT * FROM salaries ORDER BY salary LIMIT 1000;
```
```
SELECT * FROM salaries ORDER BY salary LIMIT 10000;
```

- Drop all the previously created indices


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

### Session 9 - 08/05/2024

We exercise more on complex SQL queries that requires the use of set operators, nested queries and subqueries. We used the Pizza db as test subject. We discussed conceptual approaches to generate test cases to validate our queries.
We experimented creating and modifying views.
We discussed the implications of different configurations of the referential constraint triggers (ON DELETE|ON UPDATE).
