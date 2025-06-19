from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
import os
db = SQLAlchemy()  # Instancia global de SQLAlchemy
def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../../frontend/templates"
        ),
        static_folder=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "../../frontend/static"
        )
    )
    app.config.from_object(Config)
    db.init_app(app)

    # Configura CORS para permitir solicitudes desde cualquier origen
    
    #CORS(app, resources={r"/api/*": {"origins": "*"}}) # Permite todas las rutas de la API
    #CORS(app, supports_credentials=True, origins="*") # configuracon de cors para permitir todas las rutas de la API y credenciales
    CORS(app, supports_credentials=True, origins=["http://localhost:5000", "http://127.0.0.1:5000"])

    # Importa y registra los blueprints
    from .routes.auth_routes import auth_bp
    from .routes.view_routes import view_bp
    from .routes.user_routes import user_bp #PARA ADMIN RUTAS
    app.register_blueprint(auth_bp)
    app.register_blueprint(view_bp)
    app.register_blueprint(user_bp)

    @app.errorhandler(404)
    def not_found_error(error):
        return {"error": "Recurso no encontrado"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Error interno del servidor"}, 500

    return app