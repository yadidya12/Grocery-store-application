from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()


def make_response(data):
    """Helper to jsonify with CORS enabled"""
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getUOM', methods=['GET'])
def get_uom():
    return make_response(uom_dao.get_uoms(connection))


@app.route('/getProducts', methods=['GET'])
def get_products():
    return make_response(products_dao.get_all_products(connection))


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = request.get_json()  # expecting application/json
    product_id = products_dao.insert_new_product(connection, request_payload)
    return make_response({'product_id': product_id})


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    request_payload = request.get_json()
    deleted_count = products_dao.delete_product(connection, request_payload['product_id'])
    return make_response({'deleted_count': deleted_count})


@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    return make_response(orders_dao.get_all_orders(connection))


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = request.get_json()
    order_id = orders_dao.insert_order(connection, request_payload)
    return make_response({'order_id': order_id})


if __name__ == "__main__":
    print("🚀 Starting Python Flask Server For Grocery Store Management System...")
    app.run(port=5000, debug=True)
