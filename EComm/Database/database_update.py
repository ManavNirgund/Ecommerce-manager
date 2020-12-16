from sqlite3 import Error


def user_insert(conn, user_info):
    """
    Inserts a row in 'user' table with the values passed in 'user_info'
    Also, inserts a row in the 'seller' or 'customer' table according to the type of user.

    Parameters:
        conn: Connection object
        user_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into user(user_id, user_name, email, password, phone, type)" \
              " VALUES (?, ?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, user_info)

        if user_info[-1] == "Seller":
            sql = f" INSERT into seller(user_id) VALUES ({user_info[0]}) "
            cur = conn.cursor()
            cur.execute(sql)
        elif user_info[-1] == "Customer":
            sql = f" INSERT into customer(user_id) VALUES ({user_info[0]}) "
            cur = conn.cursor()
            cur.execute(sql)

        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def user_update(conn, user_info):
    """
    Updates a row in 'user' table with the values passed in 'user_info'
    Parameters:
        conn: Connection object
        user_info: a tuple of values to update
    """
    try:
        sql = " UPDATE user SET" \
              " user_name = ? ," \
              " email = ? ," \
              " password = ? ," \
              " phone = ? " \
              " WHERE user_id = ?"
        cur = conn.cursor()
        cur.execute(sql, user_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def seller_update(conn, seller_info):
    """
    Updates a row in 'seller' table with the values passed in 'seller_info'
    Parameters:
        conn: Connection object
        seller_info: a tuple of values to update
    """
    try:
        sql = " UPDATE seller SET" \
              " cur_address_id = ? ," \
              " cur_bank_id = ? " \
              " WHERE user_id = ?"
        cur = conn.cursor()
        cur.execute(sql, seller_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def customer_update(conn, customer_info):
    """
    Updates a row in 'customer' table with the values passed in 'customer_info'
    Parameters:
        conn: Connection object
        customer_info: a tuple of values to update
    """
    try:
        sql = " UPDATE customer SET" \
              " cur_address_id = ? ," \
              " cur_payment_id = ? " \
              " WHERE user_id = ?"
        cur = conn.cursor()
        cur.execute(sql, customer_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def payment_insert(conn, payment_info):
    """
    Inserts a row in 'payment' table with the values passed in 'payment_info'
    Parameters:
        conn: Connection object
        payment_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into payment(payment_id, user_id, payment_method, payment_number)" \
              " VALUES (?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, payment_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


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
        return str(e)


def bank_detail_insert(conn, bank_info):
    """
    Inserts a row in 'bank_detail' table with the values passed in 'bank_info'
    Parameters:
        conn: Connection object
        bank_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into bank_details (bank_id, user_id, account_number, ifsc_code)" \
              " VALUES (?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, bank_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def bank_detail_update(conn, bank_info):
    """
    Updates a row in 'bank_detail' table with the values passed in 'bank_info'
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
        return str(e)


def address_insert(conn, address_info):
    """
    Inserts a row in 'address' table with the values passed in 'address_info'
    Parameters:
        conn: Connection object
        address_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into address(address_id, user_id, address, city, state, pincode)" \
              " VALUES (?, ?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, address_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


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
        return str(e)


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
        return str(e)


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
        return str(e)


def product_insert(conn, product_info):
    """
    Inserts a row in 'product' table with the values passed in 'product_info'
    Parameters:
        conn: Connection object
        product_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into product(product_id, user_id, product_name, brand, category_id," \
              " price, product_desc, tags, image)" \
              " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, product_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


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
        return str(e)


def cart_insert(conn, cart_info):
    """
    Inserts a row in 'cart' table with the values passed in 'cart_info'
    Parameters:
        conn: Connection object
        cart_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into cart(cart_id, user_id, product_id, product_qty)" \
              " VALUES (?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, cart_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def cart_update(conn, cart_info):
    """
    Updates a row in 'cart' table with the values passed in 'cart_info'
    Parameters:
        conn: Connection object
        cart_info: a tuple of values to update
    """
    try:
        sql = " UPDATE cart SET" \
              " product_id = ? ," \
              " product_qty = ? " \
              " WHERE cart_id = ?"
        cur = conn.cursor()
        cur.execute(sql, cart_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def wishlist_insert(conn, wishlist_info):
    """
    Inserts a row in 'wishlist' table with the values passed in 'wishlist_info'
    Parameters:
        conn: Connection object
        wishlist_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into wishlist(wishlist_id, user_id, product_id)" \
              " VALUES (?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, wishlist_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def order_insert(conn, order_info):
    """
    Inserts a row in 'orders' table with the values passed in 'order_info'
    Parameters:
        conn: Connection object
        order_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into orders(order_id, user_id, total_cost, address, payment, order_date)" \
              " VALUES (?, ?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, order_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def order_update(conn, order_info):
    """
    Updates a row in 'order' table with the values passed in 'order_info'
    Parameters:
        conn: Connection object
        order_info: a tuple of values to update
    """
    try:
        sql = " UPDATE orders SET" \
              " total_cost = ? ," \
              " address = ? ," \
              " payment = ? ," \
              " order_date = ? " \
              " WHERE order_id = ?"
        cur = conn.cursor()
        cur.execute(sql, order_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


def order_details_insert(conn, order_details_info):
    """
    Inserts a row in 'order_details' table with the values passed in 'order_details_info'
    Parameters:
        conn: Connection object
        order_details_info: a tuple of values to insert
    """
    try:
        sql = " INSERT into order_details(id, order_id, product_id, product_name, product_qty," \
              " product_cost, total_cost)" \
              " VALUES (?, ?, ?, ?, ?, ?, ?) "
        cur = conn.cursor()
        cur.execute(sql, order_details_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)


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
              " WHERE id = ?"
        cur = conn.cursor()
        cur.execute(sql, order_details_info)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return str(e)
