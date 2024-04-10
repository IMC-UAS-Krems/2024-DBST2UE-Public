import sqlite3

# The following tests show that NOT using fixtures, e.g., to get a fresh connection, results in a lot o boilerplate code.

def test_that_empty_db_is_empty(file_to_empty_db):
    connection = sqlite3.connect(file_to_empty_db)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Professor")
        assert len(cursor.fetchall()) == 0

    finally:
        connection.close()


def test_that_filled_db_is_not_empty(file_to_filled_db):
    connection = sqlite3.connect(file_to_filled_db)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Professor")
        assert len(cursor.fetchall()) > 0

    finally:
        connection.close()


def test_that_copied_db_is_not_empty(file_to_copy_of_existing_db):
    connection = sqlite3.connect(file_to_copy_of_existing_db)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Professor")
        assert len(cursor.fetchall()) == 2

    finally:
        connection.close()


def test_that_filling_database_actually_fills_it(factory_db):
    alessio = (123, "Alessio", "Gambi")

    # Invoke the DB Factory passing only one tuple
    db_file = factory_db([alessio])

    connection = sqlite3.connect(db_file)
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Professor")
        assert len(cursor.fetchall()) == 1

    finally:
        connection.close()

def test_show_tables(connection_to_empty_db):
        cursor = connection_to_empty_db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = cursor.fetchall()
        print(f"Result {result}")