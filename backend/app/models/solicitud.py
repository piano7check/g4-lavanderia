# backend/models/solicitud.py

from . import db
from datetime import date

class Solicitud(db.Model):
    __tablename__ = 'solicitudes'

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    fecha_solicitud = db.Column(db.Date, default=date.today)
    estado = db.Column(db.String(30), default='pendiente')

    # Relación con usuario
    usuario = db.relationship('Usuario', backref='solicitudes')