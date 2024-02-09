#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*args):
    if len(args) == 0:
        maior = 0
    else:
        c = 0
        for v in args:
            if c == 0:
                maior = v
            elif v > maior:
                maior = v
            c+=1
    print('-='*30)
    print('Analisando os valores digitados...')
    print(f'Você digitou um total de {len(args)} valores')
    print(f'Sendo eles: {args}')
    print(f'O maior valor dentre eles é: {maior}')

maior()
maior(1, 2, 3)
maior(5, 8, 1, 7)
maior(-5, -2, -1)