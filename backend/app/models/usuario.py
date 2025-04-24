# backend/app/models/usuario.py
from app.extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
