from django.conf import settings
from django.db import models


class Cadastro(models.Model):
    # dados informados pelo RH
    cpf = models.CharField(
        max_length=11, primary_key=True, help_text="Digite apenas números"
    )
    data = models.DateField(
        "data de nascimento", help_text="Use o formato: <em>DD/MM/AAAA</em>."
    )
    email = models.EmailField("e-mail", unique=True)
    matricula = models.CharField("matrícula", unique=True, max_length=9)

    # dados gerados automaticamente no momento da criação do registro
    nome = models.CharField(max_length=100)
    criado_em = models.DateTimeField("criado em:", auto_now_add=True)

    # dados atualizados pelo RH na fase de conferência dos dados
    atendido = models.BooleanField("atendido", default=False)

    class Meta:
        verbose_name = "Cadastro"
        verbose_name_plural = "Cadastros"
        ordering = ["-criado_em"]

    def __str__(self):
        return str(self.cpf)


class Dependente(models.Model):
    cpf = models.CharField("cpf do dependente", max_length=11, primary_key=True)
    nome = models.CharField(max_length=100)
    dt_nasc = models.DateField(
        "data de nascimento", help_text="Use o formato: <em>DD/MM/AAAA</em>."
    )
    criado_em = models.DateTimeField("criado em:", auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="dependentes",
    )

    class Meta:
        verbose_name = "Dependente"
        verbose_name_plural = "Dependentes"
        ordering = ["-criado_em"]

    def __str__(self):
        return self.nome
