# Generated by Django 3.1.2 on 2020-11-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mensajes',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=100)),
            ],
        ),
    ]
