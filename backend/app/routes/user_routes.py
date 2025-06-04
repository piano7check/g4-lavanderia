#PARA ADMIN RUTAS: Crear, listar, editar , eliminar usuarios
# backend/routes/user_routes.py
from flask import Blueprint, request, jsonify
from .. import db
from ..models import Usuario
from werkzeug.security import generate_password_hash
import re

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/usuarios')

# CREAR USUARIOS :
@user_bp.route('', methods=['POST'])
def crear_usuario():
    data = request.json

    # Validar campos
    nombre = data.get('nombre')
    correo = data.get('correo')
    contrasena = data.get('contrasena')
    tipo_usuario = data.get('tipo_usuario')

    if not all([nombre, correo, contrasena, tipo_usuario]):
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    if not correo.endswith('@uab.edu.bo'):
        return jsonify({'error': 'El correo debe ser institucional (@uab.edu.bo)'}), 400

    if Usuario.query.filter_by(correo=correo).first():
        return jsonify({'error': 'El correo ya está registrado'}), 409

    # Encriptar contraseña ahora si 
    hashed_password = generate_password_hash(contrasena)

    nuevo_usuario = Usuario(nombre, correo, hashed_password, tipo_usuario)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201

# 🟡 LISTAR
@user_bp.route('', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

# 🟠 EDITAR
@user_bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.correo = data.get('correo', usuario.correo)
    usuario.tipo_usuario = data.get('tipo_usuario', usuario.tipo_usuario)

    db.session.commit()
    return jsonify({'mensaje': 'Usuario actualizado'}), 200


# ELIMINAR
@user_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado'}), 200

