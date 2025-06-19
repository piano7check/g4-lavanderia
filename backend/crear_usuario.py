from app import create_app
from app.extensions import db
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    usuario_existente = Usuario.query.filter_by(correo='ariel.alvarez@uab.edu.bo').first()
    if usuario_existente:
        print("⚠️ El usuario ya existe.")
    else:
        nuevo_usuario = Usuario(
            nombre='Ariel Álvarez',
            correo='ariel.alvarez@uab.edu.bo',
            contrasena=generate_password_hash('12345678'),
            tipo_usuario='admin'
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        print("✅ Usuario creado exitosamente.")
        print(f"Nombre: {nuevo_usuario.nombre}, Correo: {nuevo_usuario.correo}, Tipo: {nuevo_usuario.tipo_usuario}")