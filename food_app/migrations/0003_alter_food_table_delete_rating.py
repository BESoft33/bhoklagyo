# Generated by Django 4.0.5 on 2022-10-21 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='food',
            table='food',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]