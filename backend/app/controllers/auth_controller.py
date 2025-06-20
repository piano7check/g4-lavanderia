from ..models.usuario import Usuario
from ..utils.auth import generar_token
from flask import current_app
from werkzeug.security import check_password_hash
import os

class AuthController:
    @staticmethod
    def login(correo, contrasena):
        if current_app.config.get("DEBUG_MODE"):  # Bypass en desarrollo
            usuario = Usuario.query.first()  # o crea uno falso si no hay
            return {
                "token": generar_token(usuario.id if usuario else 1),
                "usuario": {
                    "nombre": usuario.nombre if usuario else "Dev User",
                    "correo": usuario.correo if usuario else correo,
                    "tipo_usuario": usuario.tipo_usuario if usuario else "admin"
                }
            }

        # Modo normal (producción)
        with current_app.app_context():
            usuario = Usuario.query.filter_by(correo=correo).first()
            if usuario and check_password_hash(usuario.contrasena, contrasena):
                token = generar_token(usuario.id)
                return {
                    "token": token,
                    "usuario": {
                        "id": usuario.id, 
                        "nombre": usuario.nombre,
                        "correo": usuario.correo,
                        "tipo_usuario": usuario.tipo_usuario
                    }
                }
            return None
