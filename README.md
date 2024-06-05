# Public repository for DBST2UE 2024

## Session 13 - 12/06/24

## NoSQL - Document Database - Mongo DB

### Task 1: Setup

Start a new mongo db (server):

```
docker run --name mongodb -d mongo
```

Connect to the running server:

```
docker exec -it mongodb mongosh
```

### Task 2
Try the basic commands:

- `show dbs` Lists all available databases
- `use <db>` Switch current database to <db>
- `show collections` Print a list of all collections for current database
- `exit` Exits the started mongo and thus also the connection to the container

> Note: You can read more here: [https://www.mongodb.com/docs/manual/tutorial/getting-started/](https://www.mongodb.com/docs/manual/tutorial/getting-started/)


### Task 3

Create a new database called `ex11` by connecting to it.

Create a collection called  `movies` with the following entries.
> Hint: use `db.movies.insert( ...`

1. Title: "Fight Club", Writer: "Chuck Palahniuk", year: "1999", actors: ["Brad Pitt", "Edward Norton"]
2. Title: "Pulp Fiction", Writer: "Quentin Tarantino", year: "1994", actors: ["John Travolta", "Uma Thurman"]
3. Title:"IngloriousBasterds",Writer:"QuentinTarantino",year:"2009",actors:["Brad Pitt", "Diane Kruger", "Eli Roth"]
4. Title: "The Hobbit: An Unexpected Journey", Writer: "J.R.R. Tolkein", year: "2012", franchise: "The Hobbit"
5. Title: "The Hobbit: The Desolation of Smaug", Writer: "J.R.R. Tolkein", year: "2013", franchise: "The Hobbit"
6. Title: "The Hobbit: The Battle of the Five Armies", Writer: "J.R.R. Tolkein", year: "2012", franchise: "The Hobbit", synopsis: "Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness."
7. Title:"Pee Wee Herman's Big Adventure"
8. Title:"Avatar"

> Note: At home you can try to automatize this process using Python

### Task 4

Update the documents inside `movies` collection:

1. Add the synopsis "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug." to the move with the title "The Hobbit: An Unexpected Journey"

2. Add the synopsis "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring." to the movie with the title "The Hobbit: The Desolation of Smaug"

3. Add "Samuel L. Jackson" as an actor to the movie "Pulp Fiction"

### Task 5

Query the database with the following text search
[https://docs.mongodb.com/manual/text-search/](https://docs.mongodb.com/manual/text-search/):

1. List all movies with the word "Gandalf" in their synopsis
2. List all movies with the words "dwarves" or "hobbit" in their synopsis
3. List all movies with the word "Bilbo" but not the word "Gandalf" in their synopsis

### Task 6 

Delete the movies "Avatar" and "Pee Wee Herman's Big Adventure" from your database.

Verify that those movies indeed disappeared.


## NoSQL - Graph Database - Neo4j

### Task 1 Setup

Start a new graph database server:

```docker run --name neo --publish=7474:7474 --publish=7687:7687 --env=NEO4J_AUTH=none -d neo4j```
 
Check that everything is running ok by visiting:

`http://localhost:7474`

Use the GUI to connect to the server and then:

### Task 2

- Lists all available databases (`:dbs`)
- Connect to the `neo4j` database with (`:use <db>`)
- Show an overview of the database (`CALL db.schema.visualization()`) 

More infos at:
[https://neo4j.com/docs/cypher-manual/4.0/](https://neo4j.com/docs/cypher-manual/4.0/)
and

[https://neo4j.com/developer/get-started/](https://neo4j.com/developer/get-started/)

### Task 3

Connect to the running Neo4J with the brower.

Start by following the introduction steps of neo4j, by working through their "Movie Graph" tutorial (`:play movie graph`). 

You can also look here for a step by step guide:
[https://neo4j.com/developer/cypher/guide-cypher-basics/](https://neo4j.com/developer/cypher/guide-cypher-basics/)

Make sure to execute (and verify) the CREATE-Step before trying anything else of this exercise. 

> Note: DO NOT RUN the Clean-up step before completing the exercise, otherwise you won't have data to work with .

1. Show all nodes and their relationships in your database
2. Output the amount of created nodes
3. Output the amount of created relationships
4. Find all titles of movies in the database
5. Return all people, who acted in the Movie with the title "Sleepless in Seattle"
6. Return all actors, who acted besides "Keanu Reeves"
7. Print out the node and the amount of its relationships of the node with the largest amount of relationships
8. Insert a new movie, which is not already in the database, including its actors, director(s) and a producer


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

### Session 11 - 22/05/24

We exercised on functional dependencies and normalization by transforming a poorly designed relation into a set of interconnected ones, such that each relation is in 3NF.

We also did exercises on scheduling of transactions proving/disproving serializable schedules.

### Session 12 - 05/06/24

We solved exercises on finding/causing deadlocks with exclusive and shared locks. We experimented simulating the execution of concurrent transactions to create resource-graphs and wait-for graph, then finding deadlocks/cycles in those graphs.