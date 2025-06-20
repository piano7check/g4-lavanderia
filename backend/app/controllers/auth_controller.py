from ..models.usuario import Usuario
from ..utils.auth import generar_token
from flask import current_app
from werkzeug.security import check_password_hash  # 👈 Importante

class AuthController: 
    @staticmethod
    def login(correo, contrasena):
        with current_app.app_context():
            usuario = Usuario.query.filter_by(correo=correo).first()
            # ✅ Verificación correcta de contraseña
            if usuario and check_password_hash(usuario.contrasena, contrasena):
                token = generar_token(usuario.id)
                return {
                    "token": token,
                    "usuario": {
                        "nombre": usuario.nombre,
                        "correo": usuario.correo,
                        "tipo_usuario": usuario.tipo_usuario
                    }
                }
            return None
