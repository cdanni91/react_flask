from flask import request, jsonify
from app import app, db
from models import User

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(first_name=data['first_name'], 
                    last_name=data['last_name'],
                      age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201
