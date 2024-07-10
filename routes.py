from flask import request, jsonify
from app import app, db
from models import User

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()  # Obtiene los datos en formato JSON de la solicitud
    new_user = User(first_name=data['first_name'], 
                    last_name=data['last_name'],
                    age=data['age'])  # Crea una nueva instancia del modelo User
    db.session.add(new_user)  # Añade el nuevo usuario a la sesión de la base de datos
    db.session.commit()  # Guarda (confirma) los cambios en la base de datos
    return jsonify({'message': 'User added successfully'}), 201  # Retorna una respuesta JSON
