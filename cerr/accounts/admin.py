from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["cpf", "nome", "matricula", "email"]
    search_fields = ["cpf", "nome", "matricula", "email"]


admin.site.register(CustomUser, CustomUserAdmin)
