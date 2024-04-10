# Public repository for DBST2UE 2024

## Session 5 - 10/04/2024

### Task 1: From RM to ER and Back

#### Step 1: Lift up RM
Consider an incomplete database schema containing the following Relations:

```
Person (name, age, gender)
frequents (Person.name, pizzeria)
eats (Person.name, pizza) 
serves (pizzeria, pizza, price, allergens)
```

> NOTE: Limit gender to male/female/other

Reverse engineer a possible ER Model that could be used to generate such an incomplete Relation Model.

#### Step 2: Complete the ER Model
Complete the ER Model by adding the missing details, such as attributes, relationships, cardinality/participation constrains. Identify possible keys/superkeys, and missing strong and weak entities.

#### Step 3: Remap the (completed) ER model into RM
Make sure to select primary keys and create appropriate references (i.e., connections via primary and foreign keys) between the various Relations.

### Task 2: Implement the database in SQLite3

- Read online about which queries and SQL operators to use for creating tables and defining constraints and references.
_Hint_: SQL is used as Data Definition Language (DDL)

> Note: Refrain from using ChatGPT or similar tools; instead, face the challenge of understanding something on your own!

- Write pytest fixtures to insert data in a temporary databases. Start by having a method that creates the DB, then write additional methods to insert data.

- Discuss how one can generate test data (e.g., names of persons, pizzas, allergens, etc.). Are there datasets that can be used? Is the use of Generative AI (e.g., ChatGPT) meaningful here?

### Task 3: Relational Algebra
Making use of the following Operators:

- RENAMING(R)
- UNION (U)
- INTERSECTION (i)
- SET DIFFERENCE (/)
- PROJECTION (P)
- SELECTION (S)
- CARTESIAN PRODUCT (x)

Write the relational algebra expressions corresponding to the following queries in Natural Language and *simulate* their execution on a small dataset (from Task 2)

1. Find all pizzerias frequented by at least one person under the age of `18`.

2. Find the names of all `female`s who can eat either `mushroom` or `pepperoni` pizzas (but NOT both)

3. Find the names of all `female`s who eat both `mushroom` and `pepperoni` pizzas.

4. Find all pizzerias that serve at least one pizza that `Amy` eats for less than `$10.00`.

5. Find all pizzerias that are frequented by only `female`s or only `male`s.

6. For each person, find all pizzas the person eats that are not served by any pizzeria the person frequents. Return all such person name and pizza pairs.

7. Find the names of all people who frequent only pizzerias serving at least one pizza they eat.

8. Find the names of all people who frequent every pizzeria serving at least one pizza they eat.

9. Find the pizzeria serving the cheapest pepperoni pizza. In the case of ties, return all of the cheapest-pepperoni pizzerias.

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
