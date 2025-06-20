# backend/models/prenda_solicitud.py

from . import db

class PrendaSolicitud(db.Model):
    __tablename__ = 'prendas_solicitud'

    id = db.Column(db.Integer, primary_key=True)
    id_solicitud = db.Column(db.Integer, db.ForeignKey('solicitudes.id'), nullable=False)
    tipo_prenda = db.Column(db.String(50), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    color_descripcion = db.Column(db.String(100), nullable=False)
