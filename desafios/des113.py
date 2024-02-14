#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

#Funções
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


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mErro! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('O usuário escolheu não digitar nenhum valor.')
            return '<nenhum>'
        else:
            return valor

#Programa principal
n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1} e o número real {n2}')