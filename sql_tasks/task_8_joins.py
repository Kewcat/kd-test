import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    -- 
    select c.name, oi.order_id, sum(oi.price * oi.quantity) 
    from customers c
    left join orders o
    on c.customer_id = o.customer_id
    left join order_items oi 
    on oi.order_id = o.order_id
    group by c.name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

print(get_customer_spend())