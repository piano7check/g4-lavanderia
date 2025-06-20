# backend/models/__init__.py
from .. import db # Importar la instancia de la base de datos
# Importar modelos
from .usuario import Usuario
from .solicitud import Solicitud
from .prenda_solicitud import PrendaSolicitud
