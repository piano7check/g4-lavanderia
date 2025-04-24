from app import create_app, db

# Crea la aplicación Flask
app = create_app()

# Prueba la conexión a la base de datos
with app.app_context():
    try:
        conn = db.engine.connect()
        print("✅ ¡Conexión a MySQL exitosa!")
        conn.close()
    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")