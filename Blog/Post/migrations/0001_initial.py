# Generated by Django 4.1.7 on 2023-03-30 19:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen_portada', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
