import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_file("config.json", load=json.load)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24) # Generar una clave secreta aleatoria
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    db.init_app(app)
    migrate.init_app(app, db)

    from routes import main_bp
    app.register_blueprint(main_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
