from flask import Flask, jsonify, request

app = Flask(__name__)

# Data dummy (better take the data from database ^_^)
users = [
    {"id": 1, "name": "Leon", "email": "leon@example.com"},
    {"id": 2, "name": "Hana", "email": "hana@example.com"}
]

# Route get all user
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Route get users from ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route add new users
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    new_user["id"] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

# Route update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
