# Generated by Django 5.1 on 2024-08-25 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_alter_noticia_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='data_nascimento',
        ),
    ]