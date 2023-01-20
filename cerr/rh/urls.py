from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "rh"
urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "colaborador/",
        login_required(views.ColaboradorListView.as_view()),
        name="colaborador_list",
    ),
    path(
        "colaborador/add/",
        login_required(views.ColaboradorCreateView.as_view()),
        name="colaborador_add",
    ),
    path(
        "colaborador/<str:pk>/",
        login_required(views.ColaboradorUpdateEmailMatriculaView.as_view()),
        name="colaborador_update",
    ),
]
