from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Noticia


class NoticiaListView(ListView):
    model = Noticia
    context_object_name = "noticias"
    paginate_by = 7


def details(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    template_name = "noticias/details.html"
    return render(request, template_name, {"noticia": noticia})
