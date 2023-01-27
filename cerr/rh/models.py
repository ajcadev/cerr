from django.conf import settings
from django.db import models
from django.urls import reverse

SEXO = (
    ("M", "MASCULINO"),
    ("F", "FEMININO"),
)

OPCAO = (
    ("S", "SIM"),
    ("N", "NÃO"),
)

PARENTESCO = (
    ("01", "Cônjuge"),
    (
        "02",
        "Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 anos ou possua Declaração de União Estável",
    ),
    ("03", "Filho(a) ou enteado(a)"),
    (
        "04",
        "Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2 grau",
    ),
    (
        "06",
        "Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial",
    ),
    (
        "07",
        "Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, universitário ou cursando escola técnica de 2 grau do(a) qual detenha a guarda judicial",
    ),
    ("09", "Pais, avós e bisavós"),
    ("10", "Menor pobre do qual detenha a guarda judicial"),
    ("11", "Pessoa absolutamente incapaz, da qual seja tutor ou curador"),
    ("12", "Ex-cônjuge"),
    ("99", "Agregado/Outros"),
)

DEFICIENTE = (
    ("01", "Física"),
    ("02", "Visual"),
    ("03", "Auditiva"),
    ("04", "Mental"),
    ("05", "Intelectual"),
    ("99", "Não Deficiente"),
)


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

    sexo = models.CharField(max_length=1, choices=SEXO, default="")
    incide_IR = models.CharField(max_length=1, choices=OPCAO, default="")
    universitario = models.CharField(
        "universitário", max_length=1, choices=OPCAO, default=""
    )
    parentesco = models.CharField(max_length=2, choices=PARENTESCO, default="")
    deficiente = models.CharField(max_length=2, choices=DEFICIENTE, default="")
    salario_familia = models.CharField(max_length=1, choices=OPCAO, default="")

    class Meta:
        verbose_name = "Dependente"
        verbose_name_plural = "Dependentes"
        ordering = ["-criado_em"]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("intranet:dependente_update", args=[self.cpf])
