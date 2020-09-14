from datetime import date

class LogginMIX:
    @staticmethod
    def imprimirINFO(hora, usuario, msg: str):
        with open(f'loggin/users/{usuario}-{date.today()}.txt', 'a+') as f:
            f.write(f'{hora} INFO: {msg}')
            f.write('\n')

    @staticmethod
    def imprimirERROR(hora, usuario, msg: str):
        with open(f'loggin/users/{usuario}-{date.today()}.txt', 'a+') as f:
            f.write(f'{hora} ERROR: {msg}')
            f.write('\n')
