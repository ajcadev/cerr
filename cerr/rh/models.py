from django.db import models


class Cadastro(models.Model):
    # dados informados pelo RH
    cpf = models.CharField(max_length=11, primary_key=True, help_text="Digite apenas números")
    data = models.DateField("data de nascimento", help_text="Use o formato: <em>DD/MM/AAAA</em>.")
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
