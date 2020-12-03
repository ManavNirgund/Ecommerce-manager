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
        print(e)


def create_default_tables(conn):
    """
    create tables if they already don't exist.
    Parameters:
        conn: Connection object
    """

    create_queries = list()

    create_queries.append(""" CREATE TABLE IF NOT EXISTS users (
                                            user_id integer PRIMARY KEY,
                                            user_name varchar,
                                            email varchar,
                                            password varchar,
                                            phone integer,
                                            type varchar); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS payments (
                                        payment_id integer PRIMARY KEY,
                                        user_id integer,
                                        payment_method varchar,
                                        payment_number varchar,
                                        FOREIGN KEY (user_id) REFERENCES users (user_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS bank_details (
                                        bank_id integer PRIMARY KEY,
                                        user_id integer,
                                        account_number varchar,
                                        ifsc_code varchar,
                                        FOREIGN KEY (user_id) REFERENCES users (user_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS address (
                                        address_id integer PRIMARY KEY,
                                        user_id integer,
                                        address varchar,
                                        city varchar,
                                        state varchar,
                                        pincode integer,
                                        FOREIGN KEY (user_id) REFERENCES users (user_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS customers (
                                        user_id integer PRIMARY KEY,
                                        cur_payment_id integer,
                                        cur_address_id integer,
                                        FOREIGN KEY (cur_payment_id) REFERENCES payment (payment_id),
                                        FOREIGN KEY (cur_address_id) REFERENCES address (address_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS sellers (
                                        user_id integer PRIMARY KEY,
                                        cur_address_id integer,
                                        cur_bank_id integer,,
                                        FOREIGN KEY (cur_address_id) REFERENCES address (address_id),
                                        FOREIGN KEY (cur_bank_id)    REFERENCES bank_details (bank_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS category (
                                        category_id integer PRIMARY KEY,
                                        category_name varchar,
                                        description varchar,
                                        thumbnail varchar); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS product (
                                        product_id integer PRIMARY KEY,
                                        seller_id integer,
                                        product_name varchar,
                                        brand varchar,
                                        category_id int,
                                        price real,
                                        product_desc varchar,
                                        tags varchar,
                                        image varchar,                                        
                                        FOREIGN KEY (seller_id) REFERENCES seller (seller_id),
                                        FOREIGN KEY (category_id) REFERENCES category (category_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS cart (
                                        id integer PRIMARY KEY,
                                        cart_id integer,
                                        customer_id integer,
                                        product_id integer,
                                        item_qty integer,
                                        FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
                                        FOREIGN KEY (product_id) REFERENCES products (product_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS wishlist (
                                        wishlist_id integer PRIMARY KEY,
                                        customer_id integer,
                                        product_id integer,
                                        FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
                                        FOREIGN KEY (product_id) REFERENCES products (product_id)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS order_details (
                                        order_id integer PRIMARY KEY,
                                        product_id integer,
                                        product_name varchar,
                                        product_qty integer,
                                        product_cost real,
                                        total_cost real,
                                        FOREIGN KEY (product_id) REFERENCES products (product_id),
                                        FOREIGN KEY (product_name) REFERENCES products (product_name)); """)

    create_queries.append(""" CREATE TABLE IF NOT EXISTS orders (
                                        id integer PRIMARY KEY,
                                        order_id integer,
                                        customer_id integer,
                                        total_cost real,
                                        address_id int,
                                        payment_id int,
                                        order_date varchar,
                                        FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
                                        FOREIGN KEY (address_id) REFERENCES address (address_id),
                                        FOREIGN KEY (payment_id) REFERENCES payment (payment_id)); """)

    for queries in create_queries:
        create_table(conn, queries)
