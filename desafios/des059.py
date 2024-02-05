#Crie um programa que leia dois valores e mostre um menu na tela:[1] somar; [2] multiplicar; [3] maior; [4] novos números; {5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

n1 = int(input('Insira o valor 1: '))
n2 = int(input('Insira o valor 2: '))
opc = 0

while opc != 5:
    sleep(.5)
    print('\nMenu de opções: ')
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opc = int(input('\nEscolha uma das opções: '))
    print()
    sleep(.8)
        
    if opc == 1:
        r = n1 + n2
        print(f'A soma entre o valor {n1} e o valor {n2} é de: {r}')
    elif opc == 2:
        r = n1 * n2
        print(f'A multiplicação entre o valor {n1} e o valor {n2} é de: {r}')
    elif opc == 3:
        if n1 > n2:
            print(f'O maior número entre o valor {n1} e o valor {n2} é: {n1}')
        else:
            print(f'O maior número entre o valor {n1} e o valor {n2} é: {n2}')
    elif opc == 4:
        print(f'Digite os novos valores: ')
        n1 = int(input('Insira o valor 1: '))
        n2 = int(input('Insira o valor 2: '))
    elif opc == 5:
        print('Até a próxima!')
    else:
        print('Opção inválida! Tente novamente.')
