from django.contrib.auth.decorators import login_required
from django.urls import path

from cerr.rh.views import DependenteCreateView, DependenteListView, DependenteUpdateView

from . import views

app_name = "intranet"
urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "dependente/",
        login_required(DependenteListView.as_view()),
        name="dependente_list",
    ),
    path(
        "dependente/add/",
        login_required(DependenteCreateView.as_view()),
        name="dependente_add",
    ),
    path(
        "dependente/<str:pk>/",
        login_required(DependenteUpdateView.as_view()),
        name="dependente_update",
    ),
]
