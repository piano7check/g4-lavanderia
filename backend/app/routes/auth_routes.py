"""# backend/app/routes/auth_routes.py
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
    return jsonify({'status': 'success', 'user_id': user_id}
)
"""
from flask import Blueprint, request, jsonify
from ..models.usuario import Usuario
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta

auth_bp = Blueprint('auth', __name__)

# Configuración sencilla para JWT (¡Cambia esto en producción!)
#SECRET_KEY = "clave_secreta_uab"  # <-- Pide al equipo que la definan en config.py

# Ruta de registro (solo para administradores)
@auth_bp.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    
    # Validación básica
    if not data.get('correo') or not data.get('contrasena'):
        return jsonify({"error": "Correo y contraseña son requeridos"}), 400
    
    if not data['correo'].endswith('@uab.edu.bo'):
        return jsonify({"error": "Solo correos @uab.edu.bo"}), 400

    # Verificar si el usuario ya existe
    if Usuario.query.filter_by(correo=data['correo']).first():
        return jsonify({"error": "El correo ya está registrado"}), 400

    # Crear usuario (sin hashear la contraseña aún, lo haremos después)
    nuevo_usuario = Usuario(
        nombre=data.get('nombre', ''),
        correo=data['correo'],
        contrasena=generate_password_hash(data['contrasena']),  # <-- Hasheamos aquí
        tipo_usuario=data.get('tipo_usuario', 'estudiante')
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario creado", "id": nuevo_usuario.id}), 201

# Ruta de login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(correo=data.get('correo')).first()

    if not usuario or not check_password_hash(usuario.contrasena, data.get('contrasena', '')):
        return jsonify({"error": "Credenciales incorrectas"}), 401

    # Generar token JWT (expira en 1 hora)
    token = jwt.encode({
        'sub': usuario.id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({"token": token, "tipo_usuario": usuario.tipo_usuario}), 200