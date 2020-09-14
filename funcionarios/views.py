from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Funcionario
from .formulario import FormularioFuncionario

from loggin import log
from datetime import datetime
from . import funcs


infoLOG = log.LogginMIX()
# FIXME: Insert a Favicon.ico


@login_required
def adicionarFuncionario(request):
    """
    This view will add the user to DATABASE after fill the form. All information about the user will be registrated.
    :param request: Will receive the request from page.
    :return: Will return the render of page, if the first visit of page, will return 'adicionarfuncionario.html',
            after fill the form and click on save, it redirect to 'listFunc' page.
    """
    user = request.user.username
    form = FormularioFuncionario(request.POST or None)
    infoLOG.imprimirINFO(datetime.now(), user, 'visitou a sessao de adicionar Funcinário')
    if form.is_valid():
        try:
            form.save()
            infoLOG.imprimirINFO(datetime.now(), user,
                f'adicionou um usuario chamado: {form.cleaned_data["primeiroNome"]} {form.cleaned_data["ultimoNome"]}')
            return redirect('listFunc')
        except Exception as e:
            infoLOG.imprimirERROR(
                f'{datetime.now()}',
                user,
                f'falhou um usuario chamado: {form.cleaned_data["primeiroNome"]} {form.cleaned_data["ultimoNome"]}\n {e}'
            )
    return render(request, 'adicionarfuncionario.html', {'form': form})


# TODO: Inserir a busca por clientes por campo nome & sobrenome
#       pois atualmente ele está buscando por itens isoladamente
@login_required
def listarFuncionario(request):
    """
    This form will List all users created in the DATABASE ( after creation ), there's possible to
    Edit and Delete the user from webpage.
    :param request: Will receive the request to render the page.
    :return: Will return the
    """
    busca = request.GET.get('busca', None)
    saudacao = funcs.saudacao()
    user = request.user.username
    try:
        if busca:
            infoLOG.imprimirINFO(f'{datetime.now()}', user,
                                 f'Buscou por: "{busca}" em ListarFuncionario')
            func = Funcionario.objects.all()
            func = func.filter(primeiroNome__icontains=busca)
        else:
            infoLOG.imprimirINFO(f'{datetime.now()}', user,
                                 f'visitou a sessao de ListarFuncionario')
            func = Funcionario.objects.all()
        return render(request, 'listarfuncionario.html', {'func': func, 'saudacao': saudacao})
    except Exception as e:
        infoLOG.imprimirERROR(f'{datetime.now()}',
                              user,
                              'a Sessao de listarFuncionarios falhou ao carregar o banco de dados!')
        return render(request, 'listarfuncionario.html', {'func': func, 'saudacao': saudacao})


@login_required
def editarFuncionario(request, id):
    """
    That function will edit the user from Database. After user click in "Editar Funcionário" in ListFunc
    it will goes to that function and all forms are filledUP to change the necessary information
    :param request:
    :param id:
    :return:
    """
    saudacao = funcs.saudacao()
    user = request.user.username
    func = get_object_or_404(Funcionario, pk=id)
    form = FormularioFuncionario(request.POST or None, request.FILES or None, instance=func)
    infoLOG.imprimirINFO(f'{datetime.now()}', user,
                         f'Entrou na tela de edição do {func}')
    if form.is_valid():
        try:
            form.save()
            infoLOG.imprimirINFO(f'{datetime.now()}',
                                 user,
                                 f'O usuário {form.cleaned_data["primeiroNome"]} foi alterado!')
            return redirect('listFunc')
        except Exception as e:
            pass
    return render(request, 'editarfuncionario.html', {'form': form, 'func':func, 'saudacao': saudacao})


# TODO: Inserir a página bootstrap personalizada
@login_required
def deletarFuncionario(request, id):
    """
    This function will delete a user from database, after select to delete in webpage.

    :param request: Will receive the request to receive all information from server.
    :param id: Will receive the ID of user to be deleted.
    :return: Will return the request to render the page and the HTML of page.
    """
    saudacao = funcs.saudacao()
    user = request.user.username
    func = get_object_or_404(Funcionario, pk=id)
    infoLOG.imprimirINFO(f'{datetime.now()}', user,
            f'Entrou na tela de confirmação para deletar o {func}')
    if request.method == 'POST':
        try:
            infoLOG.imprimirINFO(f'{datetime.now()}', user,
                                 f'O usuário {func} foi DELETADO.'
                                 )
            func.delete()
            return redirect('listFunc')
        except Exception as e:
            pass
    return render(request, 'deletarfuncionario.html', {'func': func, 'saudacao': saudacao})

