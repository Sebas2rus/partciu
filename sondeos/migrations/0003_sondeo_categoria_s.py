# Generated by Django 4.1.3 on 2022-11-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sondeos', '0002_alter_sondeo_id_parametro'),
    ]

    operations = [
        migrations.AddField(
            model_name='sondeo',
            name='categoria_s',
            field=models.CharField(default='Comunitaria', max_length=50, verbose_name='Categoria'),
            preserve_default=False,
        ),
    ]
