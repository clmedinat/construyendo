# Generated by Django 4.1 on 2022-09-21 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptransacciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='empleado',
        ),
    ]