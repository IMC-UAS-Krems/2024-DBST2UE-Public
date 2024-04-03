## Session 3 - 20/03/2024

#### Task 1 - Install SQLite3 and Docker

- [ ] Install SQLite3
- [ ] Check that you can run it by running `sqlite3 --version` `sqlite3.exe --version` (?) on your shell
- [ ] Install `docker` (you need to register)
- Start docker desktop if not yet started (this is a regular app)
- Check that docker is working by running `docker ps` or `docker.exe ps` (?) on your shell
- Start the hello-world container using `docker run hello-world`. What's the message you see on your console?
- Start the mariadb:10.6 container and connect to it. Refer to [https://hub.docker.com/_/mariadb](https://hub.docker.com/_/mariadb) section: ``How to use this image''. 
- Connect to the mariadb server
- Stop the container
- Start the mariadb:10.6 contains using `docker-compose`: create a docker-compose.yml file in your repository, copy the content of the file you see at [https://hub.docker.com/_/mariadb](https://hub.docker.com/_/mariadb), follow the instructions
- Check `http://localhost:8080`
- Stop the container using `docker-compose down`
- List all the containers: `docker ps -a` and `docker ps -a -q`. What's the difference?
- Remove all the containers: `docker rm $(docker ps -a -q)`

#### Task 2 - Play around with pytest, fixture/mocks/studb

- Go to the root of your project
- Activate your `.venv` (if not yet active)
- Create a module `more_test.py` inside `tests`
- Create tests called, `test_persistent` and `test_right_setup`, inside `more_test.py`

- `test_persistent` must create a text file called `test-me.txt` and assert that the file is empty. Then, it should write inside the file the string `abc` and assert that the file is not empty (or that contains the string `abc`)

- `test_right_setup ` must create a TEMPORARY text file and assert that the file is empty. Then, it should write inside the file the string `abc` and assert that the file is not empty (or that contains the string `abc`

- Answer the question: What happens if you run the tests more than one time?

#### Task 3 - Connect to a sqlite3 database from python
- This task assumes that you have installed the `sqlite3` utility (see task 1)
> Note: `sqlite3` is a built in python package you do not have to install it

- Create a test called, `test_connect_to_sqlite3` that receives a connection to a **temporary** sqlite3 db created as fixture and list the tables in the database (see this [SO Post](https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api)

- Answer the following question: how do you ensure that the connection to the db is correctly closed after the test (and every time the fixture is used?
> Hint: **yields** is your friend

- Implement the following test fixtures that return/yield a connection to a sqlite database:

    - connection\_to\_empty\_db: creates an empty test database with the following schema (from [https://www.sqlitetutorial.net/sqlite-python/creating-tables/](https://www.sqlitetutorial.net/sqlite-python/creating-tables/):

    ```
    -- projects table
CREATE TABLE IF NOT EXISTS Project (
	id integer PRIMARY KEY,
	name text NOT NULL
	);

    -- tasks table
CREATE TABLE IF NOT EXISTS Task (
	id integer PRIMARY KEY,
	name text NOT NULL,
	priority integer,
	project_id integer NOT NULL
	FOREIGN KEY (project_id) REFERENCES Project (id)
);
    ```
    
    - connection\_to\_fresh\_test\_db: creates a test database with the same schema as the one above, but filled with test data. The test database must be backed up by temporary file and the data must be inserted using the following (parametric) query

    ```
INSERT INTO Project (id, name) VALUES(<SOME_ID>, <SOME_VALUE>);
    ```

    - connection\_to\_stored\_test\_db: creates a test database with the same schema as the one above filled with test data by copying an existing test database into a temporary file.
    > Hint: Copy the `.db` file from the previous task into your project and use that as the source database to copy around (e.g., using python [shutil](https://stackoverflow.com/questions/123198/how-to-copy-files)).

> NOTE: conftest.py enables you to share fixtures across tests. It is loaded automatically by pytest, and any fixtures defined in it are available to test modules in the same directory and below automatically.