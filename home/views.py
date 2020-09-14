from django.shortcuts import render, redirect
from django.contrib import auth
from datetime import datetime
from loggin import log

infoLog = log.LogginMIX

def home(request):
    return redirect('listFunc')

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
    