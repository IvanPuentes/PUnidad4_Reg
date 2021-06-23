# Generated by Django 3.2.4 on 2021-06-23 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mipagina', '0007_alter_comentariohosp_hospedaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarioviaje',
            name='Viaje',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comentariosViaje', to='mipagina.viaje'),
        ),
        migrations.AlterField(
            model_name='comentariovuelo',
            name='Vuelo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comentariosVuelo', to='mipagina.vuelo'),
        ),
    ]
