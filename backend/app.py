from flask import Flask
from config import Config
from extensions import db, migrate, cors
from routes import bp as api_bp
from models import *
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(api_bp)

    @app.route("/")
    def index():
        return {"status": "API running"}

    return app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    
# python app.py    
# flask run --host=0.0.0.0
