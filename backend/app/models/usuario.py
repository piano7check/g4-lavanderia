# backend/app/models/usuario.py
from .. import db  # Importa la instancia de SQLAlchemy desde __init__.py

# Modelo que representa la tabla 'usuarios' en MySQL
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(256), nullable=False)
    tipo_usuario = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'tipo_usuario': self.tipo_usuario
        }

    def __init__(self, nombre, correo, contrasena, tipo_usuario):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.tipo_usuario = tipo_usuario
