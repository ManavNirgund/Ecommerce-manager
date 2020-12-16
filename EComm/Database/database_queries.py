from sqlite3 import Error
from passlib.hash import pbkdf2_sha256


def run_query(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchall()
        return row
    except Error as e:
        print(e)
        return str(e)


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
        cur.execute(sql, email)
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
        return str(e)


def get_customer_record(conn, user_id):
    sql = "SELECT * FROM user JOIN customer ON user.user_id=customer.user_id;"
    return run_query(conn, sql)


def get_seller_record(conn, user_id):
    sql = "SELECT * FROM user JOIN seller ON user.user_id=seller.user_id;"
    return run_query(conn, sql)


def get_payment(conn, user_id):
    sql = f"SELECT * FROM payment WHERE user_id={user_id};"
    return run_query(conn, sql)


def get_bank_details(conn, user_id):
    sql = f"SELECT * FROM bank_details WHERE user_id={user_id};"
    return run_query(conn, sql)


def get_address(conn, user_id):
    sql = f"SELECT * FROM address WHERE user_id={user_id};"
    return run_query(conn, sql)


def get_category(conn):
    sql = f"SELECT * FROM category;"
    return run_query(conn, sql)


def get_product(conn, category_id=''):
    sql = f"SELECT * FROM product"
    if category_id != '':
        sql += f' WHERE category_id={category_id}'
    return run_query(conn, sql)


def get_cart(conn, user_id):
    sql = f"SELECT * FROM cart WHERE user_id={user_id};"
    return run_query(conn, sql)


def get_wishlist(conn, user_id):
    sql = f"SELECT * FROM wishlist WHERE user_id={user_id};"
    return run_query(conn, sql)


def get_orders(conn, user_id):
    sql = f"SELECT * FROM orders WHERE user_id={user_id};"
    return run_query(conn, sql)


def get_order_details(conn, order_id):
    sql = f"SELECT * FROM order_details WHERE order_id={order_id};"
    return run_query(conn, sql)
