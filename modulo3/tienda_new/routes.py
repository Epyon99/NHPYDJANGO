import os
from flask import Blueprint, current_app, flash, jsonify, redirect, render_template, request, url_for
from forms import ProductForm
from models import Producto
from app import db
from werkzeug.utils import secure_filename

main_bp = Blueprint('main', __name__)

@main_bp.route('/producto/hello', methods=['GET'])
def get_hello():
    return jsonify({
        'id': 'hello'
    })

@main_bp.route('/producto/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get_or_404(id)
    return jsonify({
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio
    })

@main_bp.route('/list')
def list():
    productos = Producto.query.all()
    return render_template('producto/product_list.html',productos=productos)

@main_bp.route('/create', methods=['GET','POST'])
def create_product():
    formulario = ProductForm()
    if formulario.validate_on_submit():
        # Guardar la imagen si existe 
        image_filename = None 
        if formulario.imagen.data: 
            image = formulario.imagen.data 
            image_filename = secure_filename(image.filename) 
            image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename)) 
        nuevo_producto = Producto()
        nuevo_producto.nombre = formulario.nombre.data
        nuevo_producto.precio=float(formulario.precio.data)
        db.session.add(nuevo_producto)
        db.session.commit()
        print (url_for('main.list'))
        return redirect(url_for('main.list'))
    return render_template('producto/product_form.html',form=formulario)    

@main_bp.route('/edit/<int:product_id>', methods=['GET','POST'])
def edit_product(product_id):
    pass

@main_bp.route('/delete/<int:product_id>', methods=['GET','POST'])
def delete_product(product_id):
    pass

@main_bp.route('/detail/<int:product_id>', methods=['GET'])
def detail_product(product_id):
    pass