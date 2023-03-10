# Generated by Django 3.2.16 on 2023-01-15 19:03

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Noticia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="título")),
                ("slug", models.SlugField(verbose_name="atalho")),
                (
                    "description",
                    tinymce.models.HTMLField(blank=True, verbose_name="notícia"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="noticias/images",
                        verbose_name="imagem",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="atualizado em"),
                ),
            ],
            options={
                "verbose_name": "Noticia",
                "verbose_name_plural": "Noticias",
                "ordering": ["-id"],
            },
        ),
    ]
