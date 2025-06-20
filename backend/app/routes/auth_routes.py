#AUTH ROUTERS:auth_routes.py     ← Login, logout, autenticación
from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import AuthController
from ..models import Usuario
from .. import db
auth_bp = Blueprint('auth_bp', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')
    result = AuthController.login(correo, contrasena)

    if result and 'usuario' in result and 'token' in result:
        usuario = result['usuario']
        return jsonify({
            "token": result['token'],
            "usuario": {
                "id": usuario['id'], 
                "nombre": usuario['nombre'],
                "correo": usuario['correo'],
                "tipo_usuario": usuario['tipo_usuario']
            }
        }), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
