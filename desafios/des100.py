#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(num):
    for c in range(0, 5):
        num.append(randint(0, 10))
    print(f'Os números sorteados foram: {num}')

def somaPar(num):
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares é: {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)
