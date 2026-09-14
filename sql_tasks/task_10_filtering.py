import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = """
    -- WRITE YOUR SQL HERE
    select email, order_date from customers c
    left join orders o
    on c.customer_id = o.customer_id
    where status = 'Pending'

    """

    
    cursor.execute(query)
    return cursor.fetchall()

print(get_pending_customers())