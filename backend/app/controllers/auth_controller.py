#Auth_Controller.py
from ..models.usuario import Usuario
from ..utils.auth import generar_token
from flask import current_app

class AuthController:#busca el usuario por correo y contraseña, genera un token si las credenciales son válidas
    @staticmethod
    def login(correo, contrasena):
        with current_app.app_context():  
            usuario = Usuario.query.filter_by(correo=correo).first()
            if usuario and usuario.contrasena == contrasena:  # sin hash por ahora
                token = generar_token(usuario.id)
                return {
                    "usuario": usuario.to_dict(),  # Aquí se convierte el usuario a un diccionario
                    "token": token
                }
        return None
    