from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)
    tipo_usuario = db.Column(db.String(20), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    
    def __init__(self, nombre, correo, contrasena, tipo_usuario='usuario', activo=True):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = generate_password_hash(contrasena)
        self.tipo_usuario = tipo_usuario
        self.activo = activo
    
    def verificar_contrasena(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'tipo_usuario': self.tipo_usuario,
            'activo': self.activo
        }