# Generated by Django 4.0.5 on 2022-06-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_adsbinfo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsbinfo',
            name='img',
            field=models.ImageField(default='img/DefaultAircraft.png', null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='adsbinfo',
            name='img_name',
            field=models.CharField(default='img_name', max_length=64, null=True),
        ),
    ]
