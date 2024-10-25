# Generated by Django 5.1.1 on 2024-10-21 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0003_alter_producto_imagen_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='producto',
        ),
        migrations.AlterField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')], default='pendiente', max_length=20),
        ),
        migrations.CreateModel(
            name='OrdenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.producto')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='productos',
            field=models.ManyToManyField(through='carrito.OrdenProducto', to='carrito.producto'),
        ),
    ]