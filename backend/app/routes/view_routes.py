# backend/app/routes/view_routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from ..utils.auth import decodificar_token
from ..models import Usuario  # Asegúrate de tener este modelo

view_bp = Blueprint('view_bp', __name__)

@view_bp.route('/')
def root():
    return render_template('auth/login.html')

@view_bp.route('/login')
def login():
    return render_template('auth/login.html')

@view_bp.route('/dashboard')
def dashboard():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return redirect(url_for('view_bp.login'))
    token = auth_header.split(' ')[1]
    user_id = decodificar_token(token)
    if not user_id:
        return redirect(url_for('view_bp.login'))
    # Busca el usuario en la base de datos
    usuario = Usuario.query.get(user_id)
    nombre = usuario.nombre if usuario else "Usuario"
    return render_template('dashboard.html', nombre=nombre)

