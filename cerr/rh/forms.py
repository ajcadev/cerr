from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms

from .models import Cadastro, Dependente


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ("cpf", "data", "email", "matricula")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Salvar"))
        self.helper.layout = Layout(
            Row(
                Column("cpf", css_class="form-group col-md-6 mb-0"),
                Column("data", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("email", css_class="form-group col-md-6 mb-0"),
                Column("matricula", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
        )


class ColaboradorUpdateEmailMatriculaForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ("email", "matricula")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Salvar"))
        self.helper.layout = Layout(
            Row(
                Column("email", css_class="form-group col-md-6 mb-0"),
                Column("matricula", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
        )


class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = ("cpf", "dt_nasc")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Salvar"))
        self.helper.layout = Layout(
            Row(
                Column("cpf", css_class="form-group col-md-6 mb-0"),
                Column("dt_nasc", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
        )


class DependenteUpdateForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = ("cpf", "dt_nasc")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Salvar"))
        self.helper.layout = Layout(
            Row(
                Column("cpf", css_class="form-group col-md-6 mb-0"),
                Column("dt_nasc", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
        )
