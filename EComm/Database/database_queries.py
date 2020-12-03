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
        seller_row, "Seller": If user exists in seller, and password is verified.
        customer_row, "Customer": If user exists in customer, and password is verified.
        "Incorrect Password": If user exists, but password is incorrect.
        "No Record Found": If user doesn't exist.
    """
    try:
        # SQL command to get user if it exists.
        sql = "SELECT * FROM customer WHERE email= ? ;"
        cur = conn.cursor()
        cur.execute(sql, (email, ))
        customer_row = cur.fetchone()
        sql = "SELECT * FROM seller WHERE email= ? ;"
        cur = conn.cursor()
        cur.execute(sql, (email,))
        seller_row = cur.fetchone()

        # Verifies the password, and returns the user details.
        if seller_row is not None:
            if pbkdf2_sha256.verify(password, seller_row[3]):
                return seller_row, "Seller"
            else:
                return "Incorrect Password"
        elif customer_row is not None:
            if pbkdf2_sha256.verify(password, customer_row[3]):
                return customer_row, "Customer"
            else:
                return "Incorrect Password"
        else:
            return "No Record Found"

    except Error as e:
        print(e)
        return -1

