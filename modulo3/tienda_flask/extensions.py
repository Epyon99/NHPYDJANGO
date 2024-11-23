
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt() 
login_manager = LoginManager() 
login_manager.login_view = 'auth.login' 