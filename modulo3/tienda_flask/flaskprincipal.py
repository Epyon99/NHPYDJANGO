from flask import Flask, redirect, url_for, request, render_template
from flask_principal import Principal, Permission, RoleNeed, identity_loaded, Identity, AnonymousIdentity, identity_changed
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'secret_key'

# Inicializar Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Inicializar Flask-Principal
principal = Principal(app)

# Definir necesidades de roles
admin_permission = Permission(RoleNeed('admin'))
editor_permission = Permission(RoleNeed('editor'))

# Modelo de usuario
class User(UserMixin):
    def __init__(self, id, roles):
        self.id = id
        self.roles = roles

# Base de datos ficticia
users = {
    '1': User('1', roles=['admin']),
    '2': User('2', roles=['editor']),
    '3': User('3', roles=[])
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Manejar identidad después del login
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    # Asignar roles a la identidad
    if current_user.is_authenticated:
        identity.provides.update(RoleNeed(role) for role in current_user.roles)
        identity.user = current_user

# Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta protegida para administradores
@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin():
    return "Bienvenido, Administrador"

# Ruta protegida para editores
@app.route('/editor')
@editor_permission.require(http_exception=403)
def editor():
    return "Bienvenido, Editor"

# Ruta para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        user = users.get(user_id)
        if user:
            login_user(user)
            identity_changed.send(app, identity=Identity(user_id))
            return redirect(url_for('index'))
    return render_template('login_2.html')

# Ruta para logout
@app.route('/logout')
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return redirect(url_for('index'))

# Manejar errores de acceso
@app.errorhandler(403)
def permission_denied(e):
    return "Acceso denegado", 403

if __name__ == '__main__':
    app.run(debug=True)
