from flask import Flask
from .extensions import db, login_manager, cors
from flask_session import Session
import os
from werkzeug.security import generate_password_hash
from .models.usuario import Usuario

def create_app():
    # Configuración de rutas base
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    
    app = Flask(
        __name__,
        static_folder=os.path.join(BASE_DIR, 'frontend/static'),
        template_folder=os.path.join(BASE_DIR, 'frontend/templates')
    )

    # Configuración básica
    app.config['SECRET_KEY'] = 'clave-super-secreta-uab2025'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:uab-2025@localhost/db_lavanderia?charset=utf8mb4'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configuración de sesión
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SECURE'] = False  # True en producción

    # Configuración CORS
    cors.init_app(app, supports_credentials=True, resources={
        r"/api/*": {
            "origins": ["http://localhost:5000", "http://127.0.0.1:5000"],
            "methods": ["GET", "POST", "OPTIONS", "PUT", "DELETE"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    })

    # Inicialización de extensiones
    db.init_app(app)
    Session(app)
    login_manager.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.session_protection = "strong"

    # Registro de blueprints
    from .routes.auth_routes import auth_bp
    from .routes.view_routes import view_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(view_bp)

    # Creación de tablas y usuario admin
    with app.app_context():
        db.create_all()
        crear_super_admin()

    return app

def crear_super_admin():
    with db.session.begin():
        correo_admin = 'admin@uab.edu.bo'
        admin_existente = Usuario.query.filter_by(correo=correo_admin).first()
        
        if not admin_existente:
            super_admin = Usuario(
                nombre='Super Admin',
                correo=correo_admin,
                contrasena=generate_password_hash('Admin123!', method='pbkdf2:sha256'),
                tipo_usuario='super_admin'
            )
            db.session.add(super_admin)
            print('✅ Super admin creado')
        else:
            print('ℹ️ El super admin ya existe')

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))