from django.shortcuts import render, redirect
from django.contrib import auth
from datetime import datetime
from loggin import log
from django.views import View

from funcionarios.models import Funcionario
from venda.models import Vendas

infoLog = log.LogginMIX

def home(request):
    return redirect('dashboard')

def logout(request):
    user = request.user.username
    try:
        infoLog.imprimirINFO(datetime.now(), user, 'se deslogou do Sistema.')
        auth.logout(request)
        return redirect('home')
    except Exception as e:
        infoLog.imprimirERROR(datetime.now(), user, f'se deslogou com erro do sistema {e}')
        auth.logout(request)
        return redirect('home')


class dashboard(View):
    def get(self, request):
        informations = {}
        informations['qntidadeFuncionarios'] = Funcionario.objects.all().count
        informations['qntidadeVendas'] = Vendas.objects.all().count
        return render(request, 'home/dashboard.html', informations)
