from backend.app import create_app
from app.routes.view_routes import view_bp

app = create_app()

if __name__ == "__main__":
    app= create_app()
    app.run(debug=True)

app.register_blueprint(view_bp)