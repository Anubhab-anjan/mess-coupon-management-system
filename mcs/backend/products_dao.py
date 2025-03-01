from sql_connection import get_sql_connection
from typing import List, Dict, Any


def get_all_orders(connection):

    cursor = connection.cursor()
    query =("SELECT * FROM mcs.orders;")

    cursor.execute(query)
    response: list[dict[str, Any]] = []

    for(student_id,student_name,total,date_time) in cursor:
        response.append(
            {
               ' student_id':student_id,
               'student_name':student_name,
               'total':total,
               'date_time':date_time
            }
        )

    return response
def insert_new_products(connection , product):
    cursor = connection.cursor()
    query = ("INSERT INTO products"
             "(name,quantity,price_per_unit)"
             "VALUES (%s,%s,%s)")
    data=(product['name'],product['quantity'],product['price_per_unit'],)
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where products_id =" + str(products_id))
    cursor.execute(query)
    connection.commit()
    
if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_new_products(connection,{
        'name': 'smothiee',
        'quantity':'90',
        'price_per_unit' : '15'
    }))
