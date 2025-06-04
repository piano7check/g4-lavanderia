#PARA ADMIN RUTAS: Crear, listar, editar , eliminar usuarios
# backend/routes/user_routes.py
from flask import Blueprint, request, jsonify
from .. import db
from ..models import Usuario

user_bp = Blueprint('user_bp', __name__, url_prefix='/api/usuarios')

@user_bp.route('/api/usuarios', methods=['POST']) # Ruta para crear un nuevo usuario que viene del frontend en usuario.js de admin
def crear_usuario():
    data = request.json
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        correo=data['correo'],
        contrasena=data['contrasena'],  #POR AHORA SIN ENCRIPTAR
        tipo_usuario=data['tipo_usuario']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado exitosamente"}), 201
