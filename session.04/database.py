def create_sqlite3_db(db_file):
    """
    Factory method that create a predefined Database schema using SQLite3

    :param db_file:
    :return:
    """
    # Not the import here!
    import sqlite3

    connection = sqlite3.connect(db_file)
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE Professor("
                       "PersNr int PRIMARY KEY,"
                       "FirstName VARCHAR(255),"
                       "LastName VARCHAR(255))")
        connection.commit()
    finally:
        connection.close()

    return db_file

def create_maria_db(username, password, db_name, network_address, network_port):
    """
    Connect to the MariaDB DBMS (server) using the given @username and @password
    at the given @network_address and @network_port.

    Create a database named @db_name if it does not exist.

    NOTE: Use the same schema that you find in create_sqlite3_db. Consider to refactor the query into a constant string
    """
    pass