#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
#Seu program tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1; b) de 10 até 0, de 2 em 2; c) uma contagem personalizada
#A contagem personalizada tem que funcionar em ordem crescente, decrescente com número positivo, descrescente com número negativo, e se entrar passo 0, que funcione com passo 1
from time import sleep


def contador(i, f, p):
    if i < f:
        print('=-'*25)
        if p == 0:
            p = 1
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont+=p
        print('FIM!')
    elif i > f:
        print('=-'*25)
        if p < 0:
            p = p * -1
        elif p == 0:
            p = 1
        print(f'Contagem de {i} até {f} de {p} em {p}')
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont-=p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
contador(i, f, p)