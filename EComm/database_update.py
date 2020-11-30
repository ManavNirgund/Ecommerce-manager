from sqlite3 import Error


def update_table(conn, create_table_query):
    """
    create a table from the create_table_query statement
    Parameters:
        conn: Connection object
        create_table_query: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_query)
    except Error as e:
        print(e)

