from django.shortcuts import render

from cerr.noticias.models import Noticia


def home(request):
    noticias = Noticia.objects.all()[:3]
    context = {"noticias": noticias}
    return render(request, "home.html", context)
