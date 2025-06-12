# g4-lavanderia

# 🧺 Sistema de Gestión de Lavandería - UAB

Este proyecto es un sistema web para gestionar el servicio de lavandería para los estudiantes internos de la Universidad Adventista de Bolivia. Cuenta con un backend desarrollado en **Python (Flask)** y un frontend en **HTML + Tailwind CSS**.

---

## 📁 Estructura del Proyecto


---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/nombre-del-repo.git
cd G4-LAVANDERIA

#dento de la capeta de backend

🐍 Backend - Python + Flask
📌 Requisitos previos

📥 Instalar dependencias
✅ Paso 1: Crear el entorno virtual
python -m venv venv

✅ Paso 2: Activar el entorno virtual
 venv/Scripts/activate

✅ Paso 3: pip install -r requirements.txt

▶️ Ejecutar el servidor
pyhton run.py

#dento de la capeta de frontend

🌐 Frontend - HTML + Tailwind CSS
📌 Requisitos
Node.js y npm

📥 Instalación de dependencias
cd frontend
npm install

▶️ Ejecutar el servidor
npm run dev

🛢️ Base de Datos - MySQL
📌 Crear base de datos y tabla de usuarios

-- Crear la base de datos con collation para soportar caracteres especiales
CREATE DATABASE db_lavanderia 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Seleccionar la base de datos
USE db_lavanderia;

-- Crear tabla usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(256) NOT NULL,
    tipo_usuario VARCHAR(50) NOT NULL
) ENGINE=InnoDB;
