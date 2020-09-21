from django import template
from datetime import datetime
from googletrans import Translator

register = template.Library()
now = datetime.now()
traducao = Translator()

# TODO: Não está atualizando corretamente
@register.simple_tag
def saudacoes():
    current_time = datetime.now().strftime("%H:%M:%S")[0:2]
    try:
        if int(current_time) >= 0 and int(current_time) < 6:
            return 'Boa madrugada,'
        elif int(current_time) >= 6 and int(current_time) < 12:
            return 'Bom dia,'
        elif int(current_time) >= 12 and int(current_time) < 18:
            return 'Boa tarde,'
        else:
            return 'Boa noite,'
    except:
        return 'Olá'


# TODO: Não está atualizando a data/hora
@register.simple_tag
def diaMesAnoHoraMinutoSegundo(formato):
    update = True
    while update == True:
        if 'September' in str(now.strftime(formato)):
            now.strftime(formato).replace('September', 'Setembro')
        return now.strftime(formato)


# TODO: Não está atualizando corretamente
@register.simple_tag
def diaCorrido(formato):
    while True:
        return now.strftime(formato)


# TODO: Não está atualizando corretamente
@register.simple_tag
def numeroSemana(formato):
    return now.strftime(formato)
