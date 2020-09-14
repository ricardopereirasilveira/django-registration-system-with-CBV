from django.http import HttpResponse

def helloNome(request, nome):
    return HttpResponse(f'Olá {nome}')


def rastrearEncomenda(request, codigo):
    return HttpResponse('')


def contaAdicao(request, valor1, valor2):
    return HttpResponse(f'{valor1} + {valor2} = {valor1 + valor2}')


def contaSubtracao(request, valor1, valor2):
    return HttpResponse(f'{valor1} - {valor2} = {valor1 - valor2}')

def horario24Horas(request, horario):
    hora = horario[0:2]
    hora = int(hora)
    if hora > 12:
        hora = hora/2
        if hora < 10:
            pass

    hora = str(f'{hora}:{horario[4:]}')
    print(hora)
    return HttpResponse(hora)