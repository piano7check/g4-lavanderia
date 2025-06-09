# backend/app/routes/view_routes.py
from flask import Blueprint, render_template, request, jsonify
from .. import db  #importa db desde el paquete app, NO desde models
from ..models import Usuario  # Solo importa Usuario desde models

view_bp = Blueprint('view_bp', __name__)

#view_bp Carga interfaces HTML (pantallas): 
@view_bp.route('/')#Agrega una ruta para / (opcional) Si queremos que la raíz muestre el login trasla ruta.
def root():
    return render_template('auth/login.html')

@view_bp.route('/login')
def login():
    return render_template('auth/login.html')# busca dentro de templates/a auth/login.html

@view_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html') #busca dentro de templates/a admin/dashboard.html

@view_bp.route('/usuarios')#carga la vista de usuarios
def usuarios():
    return render_template('admin/usuarios.html') #busca dentro de templates/a admin/usuarios.html



