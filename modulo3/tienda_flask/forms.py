from flask_wtf import FlaskForm
from wtforms import FileField, FloatField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

def floatValidator(form, field):
    try:
        number = float(field.data)
    except:
        print ("Esta pasando el validador de float")
        raise ValidationError('El valor debe ser float')

class ProductForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    descripcion = StringField("Descripcion")
    precio = FloatField("Precio", validators=[floatValidator,DataRequired()])
    imagen = FileField("Imagen")
    submit = SubmitField("Crear Produto")
    def __str__(self) -> str:
        return super().__str__()