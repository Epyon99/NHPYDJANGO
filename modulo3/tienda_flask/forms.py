from flask_wtf import FlaskForm
from wtforms import FileField, FloatField, PasswordField, StringField, SubmitField, ValidationError,EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from wtforms_sqlalchemy.fields import QueryCheckboxField,QuerySelectField,QueryRadioField,QuerySelectMultipleField

from models import Almacen, Producto, Proveedor

def floatValidator(form, field):
    try:
        number = float(field.data)
    except:
        print ("Esta pasando el validador de float")
        raise ValidationError('El valor debe ser float')

class ProductForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(),Email()])
    descripcion = StringField("Descripcion")
    precio = FloatField("Precio", validators=[floatValidator,DataRequired()])
    imagen = FileField("Imagen")
    submit = SubmitField("Crear Produto")
    proveedor = QuerySelectField('Proveedor',query_factory=lambda: Proveedor.query.all(),get_label='nombre')
    almacenes = QueryCheckboxField('Almacenes', query_factory=lambda: Almacen.query.all(), get_label='nombre')
    def validate_nombre(self,field):
        if len(field.data) < 3:
            raise ValidationError("El nombre debe tener mas de 2 caracteres")
        if "prohibido" in field.data.lower():
            raise ValidationError("El nombre no debe decir prohibido")
    def validate_descripcion(self,field):
        if len(field.data) < 3:
            raise ValidationError("El descripcion debe tener mas de 2 caracteres")
        if "prohibido" in field.data.lower():
            raise ValidationError("El descripcion no debe decir prohibido")
    def __str__(self) -> str:
        return super().__str__()

class LoginForm(FlaskForm): 
    email = StringField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)]) 
    submit = SubmitField('Login') 
    
class RegistrationForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)]) 
    email = StringField('Email', validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)]) 
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) 
    submit = SubmitField('Register')