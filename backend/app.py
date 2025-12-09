from flask import Flask
from config import Config
from extensions import db, migrate
from routes import bp as api_bp
from models import *
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # CORS (somente aqui!)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Rotas
    app.register_blueprint(api_bp)

    @app.route("/")
    def index():
        return {"status": "API running"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
