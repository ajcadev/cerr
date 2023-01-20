from django.db import models
from tinymce import models as tinymce_models


class Noticia(models.Model):
    title = models.CharField("título", max_length=100)
    slug = models.SlugField("atalho")
    description = tinymce_models.HTMLField("notícia", blank=True)
    image = models.ImageField(upload_to="noticias/images", verbose_name="imagem", null=True, blank=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("noticias:details", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ["-id"]
