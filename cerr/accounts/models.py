from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    email = models.EmailField("e-mail", unique=True)
    cpf = models.CharField("cpf", max_length=11, unique=True)
    matricula = models.CharField("matrícula", unique=True, max_length=9)
    nome = models.CharField(max_length=100)
    is_rh = models.BooleanField(default=False)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return str(self.nome)

    objects = CustomUserManager()
