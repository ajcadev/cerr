from django.urls import path

from . import views

app_name = "noticias"
urlpatterns = [
    path("", views.NoticiaListView.as_view(), name="noticia_list"),
    path("<slug:slug>/", views.details, name="details"),
]
