from sqlite3 import Error


def create_table(conn, create_table_query):
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
        print(create_table_query)
        print(e)


def create_default_tables(conn):
    """
    create tables if they already don't exist.
    Parameters:
        conn: Connection object
    """

    create_queries = list()

    create_queries.append(""" CREATE TABLE IF NOT EXISTS user (
                                        user_id integer PRIMARY KEY,
                                        user_name varchar,
                                        email varchar UNIQUE,
                                        password varchar,
                                        phone integer UNIQUE,
                                        type varchar); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS payment (
                                        payment_id integer PRIMARY KEY,
                                        user_id integer,
                                        payment_method varchar,
                                        payment_number varchar,
                                        FOREIGN KEY (user_id) REFERENCES user (user_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS bank_detail (
                                        bank_id integer PRIMARY KEY,
                                        user_id integer,
                                        account_number varchar,
                                        ifsc_code varchar,
                                        FOREIGN KEY (user_id) REFERENCES user (user_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS address (
                                        address_id integer PRIMARY KEY,
                                        user_id integer,
                                        address varchar,
                                        city varchar,
                                        state varchar,
                                        pincode integer,
                                        FOREIGN KEY (user_id) REFERENCES user (user_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS customer (
                                        user_id integer PRIMARY KEY,
                                        cur_address_id integer,
                                        cur_payment_id integer,
                                        FOREIGN KEY (cur_payment_id) REFERENCES payment (payment_id),
                                        FOREIGN KEY (cur_address_id) REFERENCES address (address_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS seller (
                                        user_id integer PRIMARY KEY,
                                        cur_address_id integer,
                                        cur_bank_id integer,
                                        FOREIGN KEY (cur_address_id) REFERENCES address (address_id),
                                        FOREIGN KEY (cur_bank_id)    REFERENCES bank_detail (bank_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS category (
                                        category_id integer PRIMARY KEY,
                                        category_name varchar,
                                        description varchar,
                                        thumbnail varchar); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS product (
                                        product_id integer PRIMARY KEY,
                                        user_id integer,
                                        product_name varchar,
                                        brand varchar,
                                        category_id int,
                                        price real,
                                        product_desc varchar,
                                        tags varchar,
                                        image varchar,
                                        FOREIGN KEY (user_id) REFERENCES user (user_id),
                                        FOREIGN KEY (category_id) REFERENCES category (category_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS cart (
                                        cart_id integer PRIMARY KEY,
                                        user_id integer,
                                        product_id integer,
                                        product_qty integer,
                                        FOREIGN KEY (user_id) REFERENCES user (user_id),
                                        FOREIGN KEY (product_id) REFERENCES product (product_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS wishlist (
                                        wishlist_id integer PRIMARY KEY,
                                        user_id integer,
                                        product_id integer,
                                        FOREIGN KEY (user_id) REFERENCES user (user_id),
                                        FOREIGN KEY (product_id) REFERENCES product (product_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS orders (
                                        order_id integer PRIMARY KEY,
                                        user_id integer,
                                        total_cost real,
                                        address varchar,
                                        payment varchar,
                                        order_date varchar,
                                        FOREIGN KEY (user_id) REFERENCES user (user_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS order_details (
                                        id integer PRIMARY KEY,
                                        order_id integer,
                                        product_id integer,
                                        product_name varchar,
                                        product_qty integer,
                                        product_cost real,
                                        total_cost real,
                                        FOREIGN KEY (order_id) REFERENCES orders (order_id),
                                        FOREIGN KEY (product_id) REFERENCES product (product_id),
                                        FOREIGN KEY (product_name) REFERENCES product (product_name)); """)

    for queries in create_queries:
        create_table(conn, queries)
