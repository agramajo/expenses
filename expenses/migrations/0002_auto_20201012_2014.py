# Generated by Django 2.2.16 on 2020-10-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='source',
            field=models.CharField(choices=[('alejandro-banco', 'Alejandro Banco'), ('alejandro-efectivo', 'Alejandro Efectivo'), ('vilma-banco', 'Vilma Banco')], max_length=20),
        ),
    ]
