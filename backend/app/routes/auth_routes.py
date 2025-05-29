from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import AuthController

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
                "nombre": usuario['nombre'],
                "correo": usuario['correo']
            }
        }), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401