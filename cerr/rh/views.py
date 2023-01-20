from datetime import datetime

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView

from .forms import CadastroForm, ColaboradorUpdateEmailMatriculaForm
from .models import Cadastro


@login_required
def index(request):
    if request.user.is_rh:
        return render(request, "rh/index.html", {})
    messages.error(
        request,
        "Você não tem permissão para acessar esta página.",
        extra_tags="alert-danger",
    )
    return render(request, "rh/access_denied.html", {})


class ColaboradorListView(ListView):
    model = Cadastro
    context_object_name = "colaboradores"
    template_name = "rh/colaborador_list.html"
    paginate_by = 5
    ordering = ["nome"]

    def get(self, request, *args, **kwargs):
        if request.user.is_rh:
            return super(ColaboradorListView, self).get(request, *args, **kwargs)
        messages.error(
            request,
            "Você não tem permissão para acessar esta página.",
            extra_tags="alert-danger",
        )
        return render(request, "rh/access_denied.html", {})


class ColaboradorCreateView(CreateView):
    model = Cadastro
    form_class = CadastroForm
    template_name = "rh/colaborador_form.html"
    success_url = reverse_lazy("rh:colaborador_list")

    def get(self, request, *args, **kwargs):
        if request.user.is_rh:
            return super(ColaboradorCreateView, self).get(request, *args, **kwargs)
        messages.error(
            request,
            "Você não tem permissão para acessar esta página.",
            extra_tags="alert-danger",
        )
        return render(request, "rh/access_denied.html", {})

    def form_valid(self, form):
        cpf = form.cleaned_data.get("cpf")
        email = form.cleaned_data.get("email")
        matricula = form.cleaned_data.get("matricula")
        password = "cerr2021"  # <-- melhorar
        data = datetime.strftime(form.cleaned_data.get("data"), "%d/%m/%Y")
        url = "https://ws.hubdodesenvolvedor.com.br/v2/cpf/?cpf={0}&data={1}&token={2}".format(
            cpf, data, settings.TOKEN_RECEITA
        )
        response = requests.get(url)
        json = response.json()
        if json["status"] and (data == json["result"]["data_nascimento"]):
            nome = json["result"]["nome_da_pf"]
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.nome = nome
            obj.save()
            # update the table accounts_customuser...
            User = get_user_model()
            try:
                User.objects.create_user(
                    username=cpf,
                    email=email,
                    password=password,
                    cpf=cpf,
                    matricula=matricula,
                    nome=nome,
                )
            except IntegrityError:
                messages.error(
                    self.request,
                    "Usuário já foi cadastrado!",
                    extra_tags="alert-danger",
                )
                return super().form_invalid(form)
            # send email to user...
            subject = "Cadastro de usuário no portal da CERR"
            context = {"nome": nome, "cpf": cpf, "password": password}
            body = render_to_string("rh/colaborador_email.txt", context)
            from_email = "Portal da CERR <" + settings.EMAIL_HOST_USER + ">"
            # to_email = email
            to_email = "cardoso.rr@hotmail.com"
            send_mail(
                subject,
                body,
                from_email,
                [to_email],
            )
        else:
            messages.error(
                self.request,
                "Desculpe, dados não conferem...",
                extra_tags="alert-danger",
            )
            return super().form_invalid(form)
        return super(ColaboradorCreateView, self).form_valid(form)


class ColaboradorUpdateEmailMatriculaView(UpdateView):
    model = Cadastro
    form_class = ColaboradorUpdateEmailMatriculaForm
    template_name = "rh/colaborador_form.html"
    success_url = reverse_lazy("rh:colaborador_list")

    def get(self, request, *args, **kwargs):
        if request.user.is_rh:
            return super(ColaboradorUpdateEmailMatriculaView, self).get(request, *args, **kwargs)
        messages.error(
            request,
            "Você não tem permissão para acessar esta página.",
            extra_tags="alert-danger",
        )
        return render(request, "rh/access_denied.html", {})

    def form_valid(self, form):
        # update the table accounts_customuser.
        cpf = self.kwargs['pk']
        User = get_user_model()
        user = User.objects.get(cpf=cpf)
        user.email = form.cleaned_data.get("email")
        user.matricula = form.cleaned_data.get("matricula")
        nome = user.nome
        password = 'cerr2021'
        try:
            user.save()
        except IntegrityError:
            messages.error(
                self.request,
                "Esta matrícula já foi cadastrada!",
                extra_tags="alert-danger",
            )
            return super().form_invalid(form)
        # send email to user.
        subject = "Cadastro de usuário no portal da CERR"
        context = {"nome": nome, "cpf": cpf, "password": password}
        body = render_to_string("rh/colaborador_email.txt", context)
        from_email = "Portal da CERR <" + settings.EMAIL_HOST_USER + ">"
        # to_email = email
        to_email = "cardoso.rr@hotmail.com"
        send_mail(
            subject,
            body,
            from_email,
            [to_email],
        )
        messages.success(
            self.request,
            "Dados atualizados com sucesso...",
            extra_tags="alert-success",
        )
        return super(ColaboradorUpdateEmailMatriculaView, self).form_valid(form)
