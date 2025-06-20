# backend/app/routes/solicitud_admin_routes.py

from flask import Blueprint, jsonify, request
from ..models import db, Solicitud, Usuario
from sqlalchemy.orm import joinedload

solicitud_admin_bp = Blueprint('solicitud_admin_bp', __name__, url_prefix='/api/admin/solicitudes')

# Obtener todas las solicitudes con nombre de usuario
@solicitud_admin_bp.route('', methods=['GET'])
def obtener_solicitudes_admin():
    try:
        solicitudes = db.session.query(Solicitud).options(joinedload(Solicitud.usuario)).all()

        resultado = []
        for s in solicitudes:
            resultado.append({
                'id': s.id,
                'id_usuario': s.id_usuario,
                'nombre_usuario': s.usuario.nombre,
                'fecha_solicitud': s.fecha_solicitud.strftime('%Y-%m-%d'),
                'estado': s.estado
            })

        return jsonify(resultado), 200

    except Exception as e:
        print("❌ Error al obtener solicitudes (admin):", e)
        return jsonify({'error': 'Error al obtener las solicitudes'}), 500


# Actualizar el estado de una solicitud
@solicitud_admin_bp.route('/<int:id_solicitud>/estado', methods=['PUT'])
def actualizar_estado_admin(id_solicitud):
    data = request.get_json()
    nuevo_estado = data.get('estado')

    if not nuevo_estado:
        return jsonify({'error': 'Estado no proporcionado'}), 400

    try:
        solicitud = Solicitud.query.get(id_solicitud)
        if not solicitud:
            return jsonify({'error': 'Solicitud no encontrada'}), 404

        solicitud.estado = nuevo_estado
        db.session.commit()
        return jsonify({'mensaje': 'Estado actualizado correctamente'}), 200

    except Exception as e:
        print("❌ Error al actualizar estado:", e)
        db.session.rollback()
        return jsonify({'error': 'Error interno al actualizar estado'}), 500
