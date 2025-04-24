import os
from pathlib import Path

# Carga .env desde la raíz del backend
dotenv_path = Path(__file__).resolve().parent.parent / '.env'
if dotenv_path.exists():
    from dotenv import load_dotenv
    load_dotenv(dotenv_path)

# backend/app/config.py
class Config:
    # Opción 1: Sin contraseña (si así configuraste MySQL)
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/db_lavanderia?charset=utf8mb4'
    
    # Opción 2: Con contraseña (recomendado)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:uab-2025@localhost/db_lavanderia?charset=utf8mb4'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False