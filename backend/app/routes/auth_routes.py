from flask import Blueprint, request, jsonify, current_app, session
from flask_login import login_user, current_user
from functools import wraps
import jwt
from datetime import datetime, timedelta
from ..models.usuario import Usuario
from ..extensions import db

auth_bp = Blueprint('auth', __name__)

def generar_token(user_id):
    payload = {
        'sub': user_id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        if not token:
            return jsonify({'status': 'error', 'message': 'Token requerido'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Usuario.query.get(data['sub'])
        except:
            return jsonify({'status': 'error', 'message': 'Token inválido'}), 401

        return f(current_user, *args, **kwargs)
    return decorated

@auth_bp.route('/login', methods=['OPTIONS'])
def login_options():
    response = jsonify({'message': 'Preflight OK'})
    return response, 200

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'correo' not in data or 'contrasena' not in data:
        return jsonify({'status': 'error', 'message': 'Faltan campos necesarios'}), 400

    usuario = Usuario.query.filter_by(correo=data['correo']).first()
    
    if not usuario or not usuario.verificar_contrasena(data['contrasena']):
        return jsonify({'status': 'error', 'message': 'Credenciales inválidas'}), 401

    login_user(usuario)
    token = generar_token(usuario.id)
    
    return jsonify({
        'status': 'success',
        'token': token,
        'user': {
            'id': usuario.id,
            'nombre': usuario.nombre,
            'correo': usuario.correo,
            'tipo_usuario': usuario.tipo_usuario
        }
    }), 200

@auth_bp.route('/logout', methods=['POST'])
@token_required
def logout(current_user):
    session.clear()
    return jsonify({'status': 'success', 'message': 'Sesión cerrada'}), 200

@auth_bp.route('/validar-token', methods=['GET'])
@token_required
def validar_token(current_user):
    return jsonify({
        'status': 'success',
        'user': {
            'id': current_user.id,
            'nombre': current_user.nombre,
            'correo': current_user.correo,
            'tipo_usuario': current_user.tipo_usuario
        }
    }), 200