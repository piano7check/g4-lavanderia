# backend/app/routes/view_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from ..utils.auth import decodificar_token  # la función que decodifica el token

view_bp = Blueprint('view_bp', __name__)

@view_bp.route('/')
def root():
    return render_template('auth/login.html')

@view_bp.route('/login')
def login():
    return render_template('auth/login.html')

@view_bp.route('/dashboard')
def dashboard():
    # Obtener el token de la sesión
    token = session.get('token')
    
    if not token:
        return redirect(url_for('view_bp.login'))

    user_id = decodificar_token(token)

    if not user_id:
        return redirect(url_for('view_bp.login'))

    return render_template('dashboard.html')

@view_bp.route('/registro')
def registro():
    return render_template('auth/registro.html')
