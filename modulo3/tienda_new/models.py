from app import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    precio = db.Column(db.Float, nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=True)
    image_filename = db.Column(db.String(100), nullable=True)
    def __repr__(self):
        return f'<Producto {self.nombre}>'

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    productos = db.relationship('Producto', backref='Proveedor', lazy=True)
    def __repr__(self):
        return f'<Proveedor {self.nombre}>'