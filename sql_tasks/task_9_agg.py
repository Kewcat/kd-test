import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = """
    -- 
    select sku, sum(quantity) from Order_Items
    group by sku
    having sum(quantity)>1

    """
    
    cursor.execute(query)
    return cursor.fetchall()

print(get_popular_skus())