import os.path

import pytest
from database import create_sqlite3_db 
import sqlite3
import shutil
import os


@pytest.fixture(scope="module")
def script_loc(request):
    """Return the directory of the currently running test script"""

    # Taken from: https://stackoverflow.com/questions/34504757/get-pytest-to-look-within-the-base-directory-of-the-testing-script
    # uses .join instead of .dirname, so we get a LocalPath object instead of
    # a string. LocalPath.join calls normpath for us when joining the path

    return request.fspath.join('..')


@pytest.fixture
def file_to_copy_of_existing_db(script_loc, tmp_path):
    """Copy an existing database from data/prefilled.db to temporary directory"""

    source_db = script_loc / "data/prefilled.db"
    assert os.path.exists(source_db)

    destination_db = tmp_path / "copied.db"

    # You copy the file over destination_db
    shutil.copyfile(source_db, destination_db)

    return destination_db


@pytest.fixture
def file_to_empty_db(tmp_path):
    """ Create an empty database with the database schema defined in session3.create_db """

    db_file = tmp_path / "test.db"

    # Invoke the factory method to create the database in the given db_file
    create_sqlite3_db (db_file)

    return db_file


@pytest.fixture
def connection_to_empty_db(file_to_empty_db):
    """ Return a connection to an empty SQLite3 db """

    connection = sqlite3.connect(file_to_empty_db)
    yield connection
    connection.close()


@pytest.fixture
def file_to_filled_db(file_to_empty_db):
    """ Create a database filled with predefined data """
    connection = sqlite3.connect(file_to_empty_db)
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Professor(PersNr, FirstName, LastName) VALUES (123, 'Foo', 'Bar')")
        cursor.execute("INSERT INTO Professor(PersNr, FirstName, LastName) VALUES (234, 'Boo', 'Far')")
        connection.commit()

    finally:
        connection.close()
    return file_to_empty_db


@pytest.fixture
def connection_to_filed_db(file_to_filled_db):
    """ Return a connection to an non-empty SQLite3 db """

    connection = sqlite3.connect(file_to_filled_db)
    yield connection
    connection.close()


@pytest.fixture
def factory_db(file_to_empty_db):
    """ Returns a factory method that create an empty database with the database schema defined in session3.create_db
    and fills it with the given data """

    def fill_me(data_to_put_in_the_database):
        """
        Get a list of tuples and insert them into the DB
        :param data_to_put_in_the_database:
        :return:
        """
        connection = sqlite3.connect(file_to_empty_db)
        try:
            cursor = connection.cursor()
            for data in data_to_put_in_the_database:
                # NOTE: the number of "?" in the query must be the same as len(data), i.e., the size of the tuple
                cursor.execute("INSERT INTO Professor VALUES (?,?,?)", data)
            connection.commit()
        finally:
            connection.close()

        return file_to_empty_db

    return fill_me