# backend/routes/solicitud_routes.py

from flask import Blueprint, request, jsonify
from ..models import db, Solicitud, PrendaSolicitud
from datetime import date

solicitud_bp = Blueprint('solicitud_bp', __name__, url_prefix='/api/solicitudes')
@solicitud_bp.route('', methods=['POST'])
def registrar_solicitud():
    data = request.get_json()

    id_usuario = data.get('id_usuario')
    prendas = data.get('prendas')


    if not id_usuario or not prendas:
        return jsonify({'error': 'Faltan datos'}), 400

    try:
        # 1. Crear la solicitud
        nueva_solicitud = Solicitud(
            id_usuario=id_usuario,
            fecha_solicitud=date.today(),
            estado='pendiente',
            
        )
        db.session.add(nueva_solicitud)
        db.session.flush()  # Para obtener el id antes de commit

        # 2. Agregar prendas vinculadas a esa solicitud
        for p in prendas:
            prenda = PrendaSolicitud(
                id_solicitud=nueva_solicitud.id,
                tipo_prenda=p['tipo_prenda'],
                cantidad=p['cantidad'],
                color_descripcion=p['color_descripcion']
            )
            db.session.add(prenda)

        db.session.commit()
        return jsonify({'mensaje': 'Solicitud registrada exitosamente'}), 201

    except Exception as e:
        db.session.rollback()
        print("Error al registrar solicitud:", e)
        return jsonify({'error': 'Error al registrar la solicitud'}), 500

# Nueva ruta para solicitudes por id_usuario
@solicitud_bp.route('/residente/<int:id_usuario>', methods=['GET'])
def obtener_solicitudes_por_usuario(id_usuario):
    try:
        solicitudes = Solicitud.query.filter_by(id_usuario=id_usuario).all()
        resultado = [{
            'id': s.id,
            'fecha_solicitud': s.fecha_solicitud.isoformat(),
            'estado': s.estado
        } for s in solicitudes]

        return jsonify(resultado), 200

    except Exception as e:
        print("Error al obtener solicitudes:", e)
        return jsonify({'error': 'Error al obtener solicitudes'}), 500