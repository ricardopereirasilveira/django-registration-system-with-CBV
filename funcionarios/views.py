from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Funcionario
from venda.models import Vendas


# FIXME: Insert a Favicon.ico


class adicionarFuncionario(CreateView):
    model = Funcionario
    template_name = 'funcionarios/adicionar-funcionario.html'
    fields = (
        'primeiroNome', 'ultimoNome', 'idade', 'email', 'profile', 'dataNascimento', 'acessarSistema',
        'rg', 'cpf'
    )
    success_url = reverse_lazy('listFunc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.user.first_name
        return context


class listarFuncionarios(ListView):
    model = Funcionario
    template_name = "funcionarios/listar-funcionario.html"

    def get_queryset(self):
        query = self.request.GET.get('busca')
        if query:
            object_list = self.model.objects.filter(primeiroNome__icontains=query) | self.model.objects.filter(ultimoNome__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.user.first_name
        return context


class editarFuncionario(UpdateView):
    model = Funcionario
    template_name = 'funcionarios/editar-funcionario.html'
    fields = [
        'primeiroNome', 'ultimoNome', 'idade', 'email', 'profile', 'dataNascimento', 'acessarSistema',
        'rg', 'cpf'
    ]
    success_url = reverse_lazy('listFunc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.user.first_name
        context['vendas'] = Vendas.objects.filter(
            person_id=2
        )
        return context


class deletarFuncionario(DeleteView):
    model = Funcionario
    template_name = 'funcionarios/deletar-funcionario.html'
    success_url = reverse_lazy('listFunc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.user.first_name
        return context