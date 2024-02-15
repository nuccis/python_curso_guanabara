def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário escolheu não digitar nenhum valor.')
            return '<nenhum>'
        else:
            return valor

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for index, item in enumerate(lista):
        print(f'\033[33m{index+1}\033[m - \033[34m{item}\033[m')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc