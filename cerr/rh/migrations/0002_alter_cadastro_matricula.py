# Generated by Django 3.2.16 on 2023-01-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rh", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cadastro",
            name="matricula",
            field=models.CharField(max_length=9, unique=True, verbose_name="matrícula"),
        ),
    ]
