import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    #app.config.from_file("flask.json",load=json.load)
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tienda_flask.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["UPLOAD_FOLDER"] = "uploads/"
    db.init_app(app)
    migrate.init_app(app,db)

    # Registrar Blueprints
    
    from productos.routes import main_bp
    app.register_blueprint(main_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
