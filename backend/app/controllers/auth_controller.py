from ..models.usuario import Usuario
from ..utils.auth import generar_token
from flask import current_app

class AuthController:
    @staticmethod
    def login(correo, contrasena):
        with current_app.app_context():  # Asegúrate de estar en el contexto de la app
            usuario = Usuario.query.filter_by(correo=correo).first()
            if usuario and usuario.contrasena == contrasena:  # sin hash por ahora
                token = generar_token(usuario.id)
                return {
                    "message": "Login exitoso",
                    "nombre": usuario.nombre,
                    "token": token
                }
        return None