import os
from pathlib import Path

# Carga .env desde la raíz del backend
dotenv_path = Path(__file__).resolve().parent.parent / '.env'
if dotenv_path.exists():
    from dotenv import load_dotenv
    load_dotenv(dotenv_path)

# backend/app/config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:uab-2025@localhost/db_lavanderia?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave_secreta_super_segura'  # Usa una cadena segura aquí
    DEBUG_MODE = True  # 🔧 Activa/desactiva  true/false login real