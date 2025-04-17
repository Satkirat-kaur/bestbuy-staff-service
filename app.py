from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# In-memory data store
staff = []

# Get all staff
@app.route('/staff', methods=['GET'])
def get_staff():
    return jsonify(staff)

# Create new staff member
@app.route('/staff', methods=['POST'])
def create_staff():
    data = request.json
    new_staff = {
        'id': str(len(staff) + 1),
        'name': data.get('name'),
        'position': data.get('position'),
        'department': data.get('department'),
        'email': data.get('email'),
        'phone': data.get('phone')
    }
    staff.append(new_staff)
    return jsonify(new_staff), 201

# Update staff member by ID
@app.route('/staff/<id>', methods=['PUT'])
def update_staff(id):
    for member in staff:
        if member['id'] == id:
            member.update(request.json)
            return jsonify(member)
    return jsonify({'error': 'Not found'}), 404

# Delete staff member by ID
@app.route('/staff/<id>', methods=['DELETE'])
def delete_staff(id):
    global staff
    staff = [member for member in staff if member['id'] != id]
    return '', 204

# Run the service
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
