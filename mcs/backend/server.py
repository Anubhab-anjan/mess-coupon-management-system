from flask import Flask , request , jsonify
import products_dao
from sql_connection import get_sql_connection
app = Flask(__name__)
connection = get_sql_connection()
@app.route('/getorders',methods=['GET'])
def get_orders():

    orders = products_dao.get_all_orders(connection)
    response = jsonify(orders)
    response.headers.add('Acess-Control-allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting python Flask Server For mess coupon management system")
    app.run(port=5000)