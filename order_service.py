from flask import Flask, jsonify

app = Flask(__name__)

# Sample orders data
orders = {
    1: {"user_id": 1, "product": "Laptop", "amount": 1200},
    2: {"user_id": 2, "product": "Smartphone", "amount": 800}
}

@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        for order_id, order in orders.items():
            user_id = order["user_id"]
            # Fetch user details from user service (if needed)
            # Since you want to be independent of user_service, you may skip this or handle gracefully
            order["user"] = {}  # Assuming no user details needed or available

        return jsonify(orders), 200  # Return orders with or without user details
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
