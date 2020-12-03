from sqlite3 import Error


def seller_insert(conn, seller_info):
    """
    Inserts a row in 'seller' table with the values passed in 'seller_info'
    Parameters:
        conn: Connection object
        seller_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into seller(seller_id, seller_name, email, password)" \
              " VALUES (?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, seller_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def customer_insert(conn, customer_info):
    """
    Inserts a row in 'customer' table with the values passed in 'customer_info'
    Parameters:
        conn: Connection object
        customer_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into customer(customer_id, customer_name, email, password)" \
              " VALUES (?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, customer_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def seller_update(conn, seller_info):
    """
    Updates a row in 'seller' table with the values passed in 'signup_seller_info'
    Parameters:
        conn: Connection object
        seller_info: a tuple of values to update
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
        cur.execute(sql, seller_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def customer_update(conn, customer_info):
    """
    Updates a row in 'customer' table with the values passed in 'customer_info'
    Parameters:
        conn: Connection object
        customer_info: a tuple of values to update
    """
    try:
        sql = " UPDATE seller SET" \
              " customer_name = ? ," \
              " email = ? ," \
              " password = ? ," \
              " phone = ? " \
              " address_id = ? ," \
              " bank_id = ? " \
              " WHERE customer_id = ?"
        cur = conn.cursor()
        cur.execute(sql, customer_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def address_insert(conn, address_info):
    """
    Inserts a row in 'address' table with the values passed in 'address_info'
    Parameters:
        conn: Connection object
        address_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into address(address_id, address, city, state, pincode)" \
              " VALUES (?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, address_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def address_update(conn, address_info):
    """
    Updates a row in 'address' table with the values passed in 'address_info'
    Parameters:
        conn: Connection object
        address_info: a tuple of values to update
    """
    try:
        sql = " UPDATE address SET" \
              " address = ? ," \
              " city = ? ," \
              " state = ? ," \
              " pincode = ? " \
              " WHERE address_id = ?"
        cur = conn.cursor()
        cur.execute(sql, address_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def payment_insert(conn, payment_info):
    """
    Inserts a row in 'payment' table with the values passed in 'payment_info'
    Parameters:
        conn: Connection object
        payment_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into payment(payment_id, payment_method, payment_number)" \
              " VALUES (?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, payment_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def payment_update(conn, payment_info):
    """
    Updates a row in 'payment' table with the values passed in 'payment_info'
    Parameters:
        conn: Connection object
        payment_info: a tuple of values to update
    """
    try:
        sql = " UPDATE payment SET" \
              " payment_method = ? ," \
              " payment_number = ? " \
              " WHERE payment_id = ?"
        cur = conn.cursor()
        cur.execute(sql, payment_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def category_insert(conn, category_info):
    """
    Inserts a row in 'category' table with the values passed in 'category_info'
    Parameters:
        conn: Connection object
        category_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into category(category_id, category_name, description, thumbnail)" \
              " VALUES (?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, category_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def category_update(conn, category_info):
    """
    Updates a row in 'category' table with the values passed in 'category_info'
    Parameters:
        conn: Connection object
        category_info: a tuple of values to update
    """
    try:
        sql = " UPDATE category SET" \
              " category_name = ? ," \
              " description = ? ," \
              " thumbnail = ? " \
              " WHERE category_id = ?"
        cur = conn.cursor()
        cur.execute(sql, category_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def bank_details_insert(conn, bank_info):
    """
    Inserts a row in 'bank_details' table with the values passed in 'bank_info'
    Parameters:
        conn: Connection object
        bank_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into bank_details (bank_id, account_number, ifsc_code)" \
              " VALUES (?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, bank_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def bank_details_update(conn, bank_info):
    """
    Updates a row in 'bank_details' table with the values passed in 'bank_info'
    Parameters:
        conn: Connection object
        bank_info: a tuple of values to update
    """
    try:
        sql = " UPDATE bank_details SET" \
              " account_number = ? ," \
              " ifsc_code = ? " \
              " WHERE bank_id = ?"
        cur = conn.cursor()
        cur.execute(sql, bank_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def product_insert(conn, product_info):
    """
    Inserts a row in 'product' table with the values passed in 'product_info'
    Parameters:
        conn: Connection object
        product_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into product(product_id, seller_id, product_name, brand, category_id," \
              " price, product_desc, tags, image)" \
              " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, product_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def product_update(conn, product_info):
    """
    Updates a row in 'product' table with the values passed in 'product_info'
    Parameters:
        conn: Connection object
        product_info: a tuple of values to update
    """
    try:
        sql = " UPDATE product SET" \
              " product_name = ? ," \
              " brand = ? ," \
              " category_id = ? ," \
              " price = ? ," \
              " product_desc = ? ," \
              " tags = ? ," \
              " image = ? " \
              " WHERE product_id = ?"
        cur = conn.cursor()
        cur.execute(sql, product_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def cart_insert(conn, cart_info):
    """
    Inserts a row in 'cart' table with the values passed in 'cart_info'
    Parameters:
        conn: Connection object
        cart_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into cart(id, cart_id, customer_id, product_id, item_qty)" \
              " VALUES (?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, cart_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def cart_update(conn, cart_info):
    """
    Updates a row in 'cart' table with the values passed in 'cart_info'
    Parameters:
        conn: Connection object
        cart_info: a tuple of values to update
    """
    try:
        sql = " UPDATE cart SET" \
              " cart_id = ? ," \
              " customer_id = ? ," \
              " product_id = ? ," \
              " item_qty = ? " \
              " WHERE id = ?"
        cur = conn.cursor()
        cur.execute(sql, cart_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def wishlist_insert(conn, wishlist_info):
    """
    Inserts a row in 'wishlist' table with the values passed in 'wishlist_info'
    Parameters:
        conn: Connection object
        wishlist_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into wishlist(wishlist_id, customer_id, product_id)" \
              " VALUES (?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, wishlist_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def wishlist_update(conn, wishlist_info):
    """
    Updates a row in 'wishlist' table with the values passed in 'wishlist_info'
    Parameters:
        conn: Connection object
        wishlist_info: a tuple of values to update
    """
    try:
        sql = " UPDATE wishlist SET" \
              " customer_id = ? ," \
              " product_id = ? " \
              " WHERE wishlist_id = ?"
        cur = conn.cursor()
        cur.execute(sql, wishlist_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def order_details_insert(conn, order_details_info):
    """
    Inserts a row in 'order_details' table with the values passed in 'order_details_info'
    Parameters:
        conn: Connection object
        order_details_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into order_details(order_id, product_id, product_name, product_qty, product_cost, total_cost)" \
              " VALUES (?, ?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, order_details_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def order_details_update(conn, order_details_info):
    """
    Updates a row in 'order_details' table with the values passed in 'order_details_info'
    Parameters:
        conn: Connection object
        order_details_info: a tuple of values to update
    """
    try:
        sql = " UPDATE order_details SET" \
              " product_id = ? ," \
              " product_name = ? ," \
              " product_qty = ? ," \
              " product_cost = ? ," \
              " total_cost = ? " \
              " WHERE order_id = ?"
        cur = conn.cursor()
        cur.execute(sql, order_details_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def orders_insert(conn, orders_info):
    """
    Inserts a row in 'orders' table with the values passed in 'orders_info'
    Parameters:
        conn: Connection object
        orders_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into orders(id, order_id, customer_id, total_cost, address_id, payment_id, order_date)" \
              " VALUES (?, ?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, orders_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1


def orders_update(conn, orders_info):
    """
    Updates a row in 'orders' table with the values passed in 'orders_info'
    Parameters:
        conn: Connection object
        orders_info: a tuple of values to update
    """
    try:
        sql = " UPDATE orders SET" \
              " customer_id = ? ," \
              " total_cost = ? ," \
              " address_id = ? ," \
              " payment_id = ? ," \
              " order_date = ? " \
              " WHERE order_id = ?"
        cur = conn.cursor()
        cur.execute(sql, orders_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return -1

