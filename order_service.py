from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

orders = {
    1: {"user_id": 1, "product": "Laptop", "amount": 1200},
    2: {"user_id": 2, "product": "Smartphone", "amount": 800}
}

USER_SERVICE_URL = "http://user_service:5001/users"

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        user_id = order["user_id"]
        user_response = requests.get(f"{USER_SERVICE_URL}/{user_id}")
        if user_response.status_code == 200:
            user = user_response.json()
            order["user"] = user
            return jsonify(order), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
