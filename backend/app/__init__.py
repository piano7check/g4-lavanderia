# backend/app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extensions import db  # Usa la instancia compartida
import os

def create_app():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    app = Flask(
        __name__,
        static_folder=os.path.join(BASE_DIR, 'frontend/static'),
        template_folder=os.path.join(BASE_DIR, 'frontend/templates')
    )

    # 🔐 Añade la SECRET_KEY (debe ser string)
    app.config['SECRET_KEY'] = 'clave-super-secreta-uab2025'
    
    # Configurar la sesión (almacenarla en el sistema de archivos)
    app.config['SESSION_TYPE'] = 'filesystem'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:uab-2025@localhost/db_lavanderia?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    from app.routes.view_routes import view_bp
    app.register_blueprint(view_bp)

    return app
