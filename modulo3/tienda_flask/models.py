from extensions import db, bcrypt
from flask_login import UserMixin

# Tabla de asociación 
almacen_producto = db.Table('almacen_producto',
                             db.Column('producto_id', db.Integer, db.ForeignKey('producto.id'), primary_key=True),
                             db.Column('almacen_id', db.Integer, db.ForeignKey('almacen.id'), primary_key=True) )
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80),unique=True,nullable=False)
    descripcion = db.Column(db.String(200),nullable=True)
    precio = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String(200),nullable=True)
    proveedor_id = db.Column(db.Integer,db.ForeignKey('proveedor.id'),nullable=True)
    def __repr__(self):
        return f'<Producto {self.nombre}>'

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80),unique=True,nullable=False)
    direccion = db.Column(db.String(200),nullable=True)
    telefono = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100),nullable=True)
    productos = db.relationship('Producto',backref='Proveedor', lazy=True)
    def __repr__(self):
        return f'<Proveedor {self.nombre}>'
    
class Almacen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True,nullable=False)
    productos = db.relationship('Producto', secondary=almacen_producto,backref=db.backref('almacenes', lazy='dynamic'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    edad = db.Column(db.Integer)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
