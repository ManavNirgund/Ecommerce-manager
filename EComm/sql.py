import sqlite3
from sqlite3 import Error
from create_database import create_default_tables


def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    Parameters:
        db_file: database file
    Returns:
        conn: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


if __name__ == '__main__':
    connection = create_connection(r"ecomm.sql")
    if connection is None:
        print("Connection cannot be established")
    create_default_tables(connection)

