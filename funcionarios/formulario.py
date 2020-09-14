from django.forms import ModelForm
from .models import Funcionario

class FormularioFuncionario(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['primeiroNome', 'ultimoNome', 'idade', 'email', 'profile', 'dataNascimento', 'acessarSistema']