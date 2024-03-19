# Session 2 - 13/03/2024

#### Task 1 - Setup a python project and test it
https://github.com/github/gitignore/blob/main/Python.gitignore

- Go to the root of your project
- Add the content of `public/.gitignore` to your `.gitignore` (or replace it entirely with the one in `public`
- Activate your `.venv` (if not yet active)
- Create the module `traits` 
- Create the folder `tests` 
- Copy `public/session.02/app.py` into `traits` and `public/session.02/test_smoke-test.py` into `tests`
- run `pytest` from the root of your project. What happens?
- Solve the problem (collaboratively)
- Deactivate your `.venv`
 
#### Task 2 - Measure test coverage
- Go to the root of your project
- Activate your `.venv` (if not yet active)
- Measure the code coverage achieved by smoke-test.py (check [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/index.html))
- Create an HTML report
> Note: You should not report achieved coverage of your own tests or empty files (like `__init__.py`). Make sure you do not do it!


#### Task 3 - Install the Additional Dependencies

- Install SQLite3
- Check that you can run it by running `sqlite3 --version` `sqlite3.exe --version` (?) on your shell
- Install docker app (you need to register)
- Start docker desktop if not yet started (this is a regular app)
- Check that docker is working by running `docker ps` or `docker.exe ps` (?) on your shell

#### Task 4 - Play around with pytest, fixture/mocks/studb

- Go to the root of your project
- Activate your `.venv` (if not yet active)
- Create a module `more_test.py` inside `tests`
- Create tests called, `test_persistent` and `test_right_setup`, inside `more_test.py`

- `test_persistent` must create a text file called `test-me.txt` and assert that the file is empty. Then, it should write inside the file the string `abc` and assert that the file is not empty

- `test_right_setup ` must create a TEMPORARY text file and assert that the file is empty. Then, it should write inside the file the string `abc` and assert that the file is not empty

- Answer the question: What happens if you run the tests more than one time?

#### Task 5 (Optional) - Connect to a sqlite3 database from python
- This task assumes that you have installed the `sqlite3` utility (see task 2)
> Note: `sqlite3` is a built in python package you do not have to install it

- Create a test called, `test_connect_to_sqlite3` that receives a connection to a **temporary** sqlite3 db created as fixture and list the tables in the database (see this [SO Post](https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api)

- Answer the following question: how do you ensure that the connection to the db is correctly closed after the test (and every time the fixture is used?
> Hint: **yields** is your friend