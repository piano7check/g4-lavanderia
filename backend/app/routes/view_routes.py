from flask import Blueprint, render_template, request, redirect, url_for, session
from ..utils.auth import decodificar_token
from ..models.usuario import Usuario

view_bp = Blueprint('view_bp', __name__)

@view_bp.route('/')
def root():
    return render_template('auth/login.html')

@view_bp.route('/login')
def login():
    return render_template('auth/login.html')

@view_bp.route('/dashboard')
def dashboard():
    token = session.get('token')
    if not token:
        return redirect(url_for('view_bp.login'))

    user_id = decodificar_token(token)
    if not user_id:
        return redirect(url_for('view_bp.login'))

    usuario = Usuario.query.get(user_id)
    if not usuario:
        return redirect(url_for('view_bp.login'))

    if usuario.tipo_usuario == 'super_admin':
        return render_template('super/dashboard.html')
    elif usuario.tipo_usuario == 'administrador':
        return render_template('admin/dashboard.html')
    else:
        return render_template('student/dashboard.html')

@view_bp.route('/registro')
def registro():
    return render_template('auth/registro.html')
