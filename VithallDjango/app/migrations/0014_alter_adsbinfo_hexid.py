# Generated by Django 4.0.5 on 2022-06-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_adsbinfo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsbinfo',
            name='HexID',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
