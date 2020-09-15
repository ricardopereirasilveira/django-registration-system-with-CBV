from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Funcionario
from .formulario import FormularioFuncionario

from loggin import log
from datetime import datetime
from . import funcs


infoLOG = log.LogginMIX()
# FIXME: Insert a Favicon.ico


class adicionarFuncionario(CreateView):
    model = Funcionario
    template_name = 'funcionarios/adicionar-funcionario.html'
    fields = [
        'primeiroNome', 'ultimoNome', 'idade', 'email', 'profile', 'dataNascimento', 'acessarSistema',
        'rg', 'cpf'
    ]
    success_url = reverse_lazy('listFunc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.user.first_name
        return context


class listarFuncionarios(ListView):
    model = Funcionario
    template_name = "funcionarios/listar-funcionario.html"

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
        return context


class deletarFuncionario(DeleteView):
    model = Funcionario
    template_name = 'funcionarios/deletar-funcionario.html'
    success_url = reverse_lazy('listFunc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.user.first_name
        return context


#
# # TODO: Inserir a página bootstrap personalizada
# @login_required
# def deletarFuncionario(request, id):
#     """
#     This function will delete a user from database, after select to delete in webpage.
#
#     :param request: Will receive the request to receive all information from server.
#     :param id: Will receive the ID of user to be deleted.
#     :return: Will return the request to render the page and the HTML of page.
#     """
#     saudacao = funcs.saudacao()
#     user = request.user.username
#     func = get_object_or_404(Funcionario, pk=id)
#     infoLOG.imprimirINFO(f'{datetime.now()}', user,
#             f'Entrou na tela de confirmação para deletar o {func}')
#     if request.method == 'POST':
#         try:
#             infoLOG.imprimirINFO(f'{datetime.now()}', user,
#                                  f'O usuário {func} foi DELETADO.'
#                                  )
#             func.delete()
#             return redirect('listFunc')
#         except Exception as e:
#             pass
#     return render(request, 'deletarfuncionario.html', {'func': func, 'saudacao': saudacao})
#
