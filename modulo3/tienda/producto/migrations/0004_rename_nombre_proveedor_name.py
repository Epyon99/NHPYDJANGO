# Generated by Django 5.1.3 on 2024-11-14 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_proveedor_delete_marca_producto_proveedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='nombre',
            new_name='name',
        ),
    ]
