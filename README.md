# Public repository for DBST2UE 2024

## Session 8 - 24/04/2024

### Task 1: More on Relational Algebra

Making use of the following Operators:

- RENAMING(R)
- UNION (U)
- INTERSECTION (i)
- SET DIFFERENCE (/)
- PROJECTION (P)
- SELECTION (S)
- CARTESIAN PRODUCT (x)

Write the relational algebra expressions corresponding to the following queries in Natural Language and *simulate* their execution on a small dataset.

As a remark, the Relational Model is the following one:

```
Person (name, age, gender)
frequents (Person.name, pizzeria)
eats (Person.name, pizza) 
serves (pizzeria, pizza, price, allergens)
```


1. Find all pizzerias frequented by at least one person under the age of `18`. - Done

2. Find the names of all `female`s who can eat either `mushroom` or `pepperoni` pizzas (but NOT both). - Done

3. Find the names of all `female`s who eat both `mushroom` and `pepperoni` pizzas.

4. Find all pizzerias that serve at least one pizza that `Amy` eats for less than `$10.00`.

5. Find all pizzerias that are frequented by only `female`s or only `male`s.

6. For each person, find all pizzas the person eats that are not served by any pizzeria the person frequents. Return all such person name and pizza pairs.

7. Find the names of all people who frequent only pizzerias serving at least one pizza they eat.

8. Find the names of all people who frequent every pizzeria serving at least one pizza they eat.

9. Find the pizzeria serving the cheapest pepperoni pizza. In the case of ties, return all of the cheapest-pepperoni pizzerias.

### Task 2: SQL as Data Definition Language (DDL)

Using SQLIte, implement the `pizza_connection.sql` database from the above Relational Model.

Make sure to define tables with appropriate attributes, domains, constraints, and so on.

### Task 3: SQL as Data Manipulation Language (DML)

Fill up the database with some data. Find a way to automatically generate data but ensure that the referential  integrity, type, and domain  constrains are met!

### Task 4: SQL as Query Language (QL)

Implement the queries from Task 1 into SQL and run them on the `pizza_connection.sql`. If you realize the queries are wrong (i.e., you have a counter example), fix them in SQL and in Relational Algebra.

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

