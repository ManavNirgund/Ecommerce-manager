from sqlite3 import Error
from passlib.hash import pbkdf2_sha256


def verify_user(conn, email, password):
    """
    Verifies the user using the email, password passed.
    Returns the user information if verified.
    If the password is wrong, or user doesn't exists, returns appropriate message.

    Parameters
        conn: the database connection object
        email: the email of the user
        password: the password of the user
    Returns
        row: If user exists, and password is verified.
        "Incorrect Password": If user exists, but password is incorrect.
        "No Record Found": If user doesn't exist.
    """
    try:
        # SQL command to get user if it exists.
        sql = "SELECT * FROM user WHERE email= ? ;"
        cur = conn.cursor()
        cur.execute(sql, (email, ))
        row = cur.fetchone()

        # Verifies the password, and returns the user details.
        if row is not None:
            if pbkdf2_sha256.verify(password, row[3]):
                return row
            else:
                return "Incorrect Password"
        else:
            return "No Record Found"

    except Error as e:
        print(e)
        return -1


def get_all_address(conn):
    try:
        # SQL command to get user if it exists.
        sql = "SELECT * FROM address WHERE email= ? ;"
        cur = conn.cursor()
        cur.execute(sql, )

    except Error as e:
        print(e)
        return -1
