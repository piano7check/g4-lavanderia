#Auth_Controller.py
from ..models.usuario import Usuario
from ..utils.auth import generar_token
from flask import current_app

class AuthController: 
    @staticmethod
    def login(correo, contrasena):
        with current_app.app_context():
            usuario = Usuario.query.filter_by(correo=correo).first()
            if usuario and usuario.contrasena == contrasena:
                token = generar_token(usuario.id)  # o como lo tengas implementado
                return {
                    "token": token,
                    "usuario": {
                        "nombre": usuario.nombre,
                        "correo": usuario.correo,
                        "tipo_usuario": usuario.tipo_usuario  # 👈 ¡Este campo es clave!
                    }
    }
            return None
        
        