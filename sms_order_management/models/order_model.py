from database.db import get_connection

def create_order(order_id, phone, product, quantity):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO orders
    (order_id, customer_phone, product, quantity, status)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (order_id, phone, product, quantity, "Pending")
    )

    conn.commit()
    conn.close()


def get_all_orders():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM orders")

    orders = cursor.fetchall()

    conn.close()

    return orders
def assign_driver(order_id, driver_name):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE orders
    SET driver_name=%s,
        status='Assigned'
    WHERE order_id=%s
    """

    cursor.execute(
        query,
        (driver_name, order_id)
    )

    conn.commit()
    conn.close()

def get_order_by_id(order_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM orders
    WHERE order_id=%s
    """

    cursor.execute(query, (order_id,))

    order = cursor.fetchone()

    conn.close()

    return order    
def update_status(order_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE orders
    SET status=%s
    WHERE order_id=%s
    """

    cursor.execute(
        query,
        (status, order_id)
    )

    conn.commit()
    conn.close()