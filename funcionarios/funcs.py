from datetime import datetime


def saudacao():
    current_time = datetime.now().strftime("%H:%M:%S")[0:2]
    try:
        if int(current_time) >= 0 and int(current_time) < 6:
            return 'Boa madrugada,'
        elif int(current_time) >= 6 and int(current_time) < 12:
            return 'Bom dia,'
        elif int(current_time) >= 12 and int(current_time) < 18:
            return 'Boa tarde,'
        else:
            return 'Boa noite'
    except:
        return 'Olá'