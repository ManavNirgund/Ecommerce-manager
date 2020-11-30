from sqlite3 import Error


def seller_signup(conn, signup_seller_info):
    """
    Inserts a row in 'seller' table with the values passed in 'signup_seller_info'
    Parameters:
        conn: Connection object
        signup_seller_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into seller(seller_id, seller_name, email, password)" \
              " VALUES (?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, signup_seller_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def customer_signup(conn, signup_customer_info):
    """
    Inserts a row in 'customer' table with the values passed in 'signup_customer_info'
    Parameters:
        conn: Connection object
        signup_customer_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into customer(customer_id, customer_name, email, password)" \
              " VALUES (?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, signup_customer_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def seller_update(conn, update_seller_info):
    """
    Updates a row in 'seller' table with the values passed in 'signup_seller_info'
    Parameters:
        conn: Connection object
        update_seller_info: a tuple of values to update
    """
    try:
        sql = " UPDATE seller SET" \
              " seller_name = ? ," \
              " email = ? ," \
              " password = ? ," \
              " address_id = ? ," \
              " bank_id = ? ," \
              " phone = ? " \
              " WHERE seller_id = ?"
        cur = conn.cursor()
        cur.execute(sql, update_seller_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def customer_update(conn, update_customer_info):
    """
    Updates a row in 'customer' table with the values passed in 'update_customer_info'
    Parameters:
        conn: Connection object
        update_customer_info: a tuple of values to update
    """
    try:
        sql = " UPDATE seller SET" \
              " customer_name = ? ," \
              " email = ? ," \
              " password = ? ," \
              " phone = ? " \
              " address_id = ? ," \
              " bank_id = ? ," \
              " WHERE customer_id = ?"
        cur = conn.cursor()
        cur.execute(sql, update_customer_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1

