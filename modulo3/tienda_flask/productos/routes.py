import os
from flask import Blueprint, current_app, jsonify, redirect, render_template, url_for, request

from forms import ProductForm
from models import Producto
from app import db
from werkzeug.utils import secure_filename


main_bp = Blueprint('productos',__name__)

@main_bp.route('/productos/hello', methods=['GET'])
def get_hello():
    return jsonify({
        "id":"hello"
    })

@main_bp.route('/productos/create', methods=['GET','POST'])
def create_producto():
    form = ProductForm()
    if (form.validate_on_submit()):
        # Procesar la imagen
        image_filename = None
        if form.imagen.data:
            image_filename = form.imagen.data            
            #image_filename = secure_filename(image)
            #print (request.files)
            #for v in request.files:
                #print (v)
            #image_data = request.files[0].read()
            #open (os.path.join(os.path.join(current_app.config['UPLOAD_FOLDER'],image_filename)), 'w').write(image_data)
        # Creacion del producto
        nuevo_producto = Producto()
        nuevo_producto.nombre = form.nombre.data
        nuevo_producto.precio = float(form.precio.data)
        nuevo_producto.descripcion = form.descripcion.data
        nuevo_producto.image_path = image_filename
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for("productos.list_producto"))
    return render_template('productos/product_form.html',form=form)

@main_bp.route('/productos/list', methods=['GET','POST'])
def list_producto():
    productos = Producto.query.all()
    return render_template("productos/product_list.html", productos=productos)

@main_bp.route("/productos/delete/<int:product_id>", methods=['GET','POST','DELETE'])
def delete_producto(product_id):
    if request.method == 'POST':
        producto = Producto.query.get_or_404(product_id)
        db.session.delete(producto)
        db.session.commit()
    return redirect(url_for("productos.list_producto"))
