from flask_wtf import FlaskForm
from wtforms import FileField, FloatField, IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    descripcion = TextAreaField('Descripcion')
    precio = FloatField('Precio',validators=[DataRequired()])
    imagen = StringField('Imagen')
    proveedor_id = IntegerField('Proveedor')
    imagen = FileField('Imagen')
    submit = SubmitField('Crear Producto')
    def __str__(self) -> str:
        return super().__str__()
