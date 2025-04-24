from flask import request, jsonify
from werkzeug.security import generate_password_hash
from ..models.usuario import db, Usuario

class AuthController:
    
    @staticmethod
    def registrar_usuario(data):
        nombre = data.get('nombre')
        correo = data.get('correo')
        contrasena = data.get('contrasena')
        tipo_usuario = data.get('tipo_usuario')

        # Validacionesfrom flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.usuario import db, Usuario

class AuthController:
    
    @staticmethod
    def registrar_usuario(data):
        nombre = data.get('nombre')
        correo = data.get('correo')
        contrasena = data.get('contrasena')
        tipo_usuario = data.get('tipo_usuario')

        # Validaciones
        if not all([nombre, correo, contrasena, tipo_usuario]):
            raise ValueError('Todos los campos son obligatorios')

        if not correo.endswith('@uab.edu.bo'):
            raise ValueError('El correo debe ser institucional (@uab.edu.bo)')

        # Verificar si el correo ya está registrado
        usuario_existente = Usuario.query.filter_by(correo=correo).first()
        if usuario_existente:
            raise ValueError('El correo ya está registrado')

        # Hashear la contraseña
        contrasena_hash = generate_password_hash(contrasena)

        # Crear el nuevo usuario
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena_hash, tipo_usuario=tipo_usuario)

        # Guardar en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        return nuevo_usuario

    @staticmethod
    def login(correo, contrasena):
        # Buscar al usuario por correo
        usuario = Usuario.query.filter_by(correo=correo).first()

        # Verificar si el usuario existe y si la contraseña es correcta
        if usuario and check_password_hash(usuario.contrasena, contrasena):  # Verifica la contraseña
            return usuario
        return None

        if not all([nombre, correo, contrasena, tipo_usuario]):
            raise ValueError('Todos los campos son obligatorios')

        if not correo.endswith('@uab.edu.bo'):
            raise ValueError('El correo debe ser institucional (@uab.edu.bo)')

        # Verificar si el correo ya está registrado
        usuario_existente = Usuario.query.filter_by(correo=correo).first()
        if usuario_existente:
            raise ValueError('El correo ya está registrado')

        # Hashear la contraseña
        contrasena_hash = generate_password_hash(contrasena)

        # Crear el nuevo usuario
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena_hash, tipo_usuario=tipo_usuario)

        # Guardar en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        return nuevo_usuario
