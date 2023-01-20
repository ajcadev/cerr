from django.contrib import admin

from .models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "created_at"]
    search_fields = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Noticia, NoticiaAdmin)
