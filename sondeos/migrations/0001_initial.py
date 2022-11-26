# Generated by Django 4.1.3 on 2022-11-23 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rango_p', models.CharField(blank=True, choices=[('MENOR QUE', 'Menor a '), ('MAYOR QUE', 'Mayor a ')], max_length=50, verbose_name='Rango de edad')),
                ('edad_p', models.IntegerField(blank=True, verbose_name='Edad')),
                ('genero_p', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('IT', 'Intersexual'), ('I', 'Indefinido'), ('N', 'Prefiero no decir')], max_length=50, verbose_name='Genero')),
                ('etnia_p', models.CharField(blank=True, choices=[('NINGUNA', 'Ninguno'), ('AFRO', 'Afro'), ('INDIGENA', 'Indigena'), ('RAIZAL', 'Raizal'), ('PALENQUERO', 'Palenquero'), ('GITANO', 'Gitano')], max_length=50, verbose_name='Etnia')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=100, verbose_name='Pregunta - Tema')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name_plural': 'Temas',
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Sondeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_s', models.CharField(max_length=50, verbose_name='Nombre del sondeo')),
                ('descripcion_s', models.CharField(max_length=500, verbose_name='Descripción del sondeo')),
                ('fecha_publicacion_s', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha y hora de publicación')),
                ('fecha_cierre_s', models.DateTimeField(verbose_name='Fecha y hora de cierre')),
                ('imagen', models.ImageField(upload_to='static/db', verbose_name='Icono del sondeo')),
                ('id_parametro', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sondeos.parametros')),
                ('id_pregunta', models.ManyToManyField(to='sondeos.tema')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta_Sondeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta1', models.CharField(max_length=250, verbose_name='respuesta')),
                ('respuesta2', models.CharField(blank=True, max_length=250, null=True, verbose_name='respuesta')),
                ('respuesta3', models.CharField(blank=True, max_length=250, null=True, verbose_name='respuesta')),
                ('respuesta4', models.CharField(blank=True, max_length=250, null=True, verbose_name='respuesta')),
                ('respuesta5', models.CharField(blank=True, max_length=250, null=True, verbose_name='respuesta')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('sondeo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sondeos.sondeo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.TextField(verbose_name='Respuesta')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sondeos.tema')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]