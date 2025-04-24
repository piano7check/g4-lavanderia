# backend/app/routes/auth_routes.py
from flask import Blueprint, request, jsonify, current_app, session
from ..controllers.auth_controller import AuthController
from ..utils.auth import generar_token
from functools import wraps
import jwt

auth_bp = Blueprint('auth', __name__)

# Middleware para verificar token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'status': 'error', 'message': 'Token requerido'}), 401

        try:
            token = auth_header.split(" ")[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user_id = data['sub']
        except jwt.ExpiredSignatureError:
            return jsonify({'status': 'error', 'message': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'status': 'error', 'message': 'Token inválido'}), 401

        return f(user_id, *args, **kwargs)
    return decorated

# Registro de usuario
@auth_bp.route('/usuarios', methods=['POST'])
def usuario():
    try:
        data = request.get_json()
        usuario = AuthController.registrar_usuario(data)
        return jsonify({
            'status': 'success',
            'data': usuario.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'correo' not in data or 'contrasena' not in data:
        return jsonify({'status': 'error', 'message': 'Faltan campos necesarios'}), 400

    usuario = AuthController.login(data['correo'], data['contrasena'])
    if not usuario:
        return jsonify({'status': 'error', 'message': 'Credenciales inválidas'}), 401

    token = generar_token(usuario.id)

    # Guardar token en session
    session['token'] = token

    return jsonify({
        'status': 'success',
        'token': token,
        'user': usuario.to_dict()
    })

# Validar token
@auth_bp.route('/validar-token', methods=['GET'])
@token_required
def validar_token(user_id):
    return jsonify({'status': 'success', 'user_id': user_id})
