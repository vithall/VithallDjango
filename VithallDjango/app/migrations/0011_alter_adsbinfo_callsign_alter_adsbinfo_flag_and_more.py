# Generated by Django 4.0.5 on 2022-06-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_adsbinfo_img_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsbinfo',
            name='Callsign',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='adsbinfo',
            name='Flag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='adsbinfo',
            name='Registration',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='adsbinfo',
            name='Type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
