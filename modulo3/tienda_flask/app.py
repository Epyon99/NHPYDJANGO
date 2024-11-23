import os
from flask import Flask
from extensions import db,migrate,bcrypt,login_manager
from flask_talisman import Talisman

import extensions
from flaskprincipal import admin
from models import User

def create_app():
    app = Flask(__name__)
    #Talisman(app)
    #app.config.from_file("f.json",load=json.load)
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tienda_flask.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["UPLOAD_FOLDER"] = "uploads/"
    app.config["WTF_CSRF_ENABLED"] = True
    app.config["REMEMBER_COOKIE_DURATION"] = "1 d"
    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app) 
    login_manager.init_app(app) 
    
    # Registrar Blueprints
    from auth import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from productos.routes import main_bp
    app.register_blueprint(main_bp)
    return app

# Definir la función user_loader 
@login_manager.user_loader 
def load_user(user_id): 
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
