# Generated by Django 4.0.5 on 2022-06-28 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_adsbinfo_photo_adsbinfo_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adsbinfo',
            name='img',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.ImageField(default='DefaultAircraft.png', upload_to='img/')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.adsbinfo')),
            ],
        ),
    ]
