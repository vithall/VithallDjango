# Generated by Django 4.0.5 on 2022-06-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adsbinfo',
            name='photo',
            field=models.ImageField(default='DefaultAircraft.png', upload_to='photos'),
        ),
    ]