#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
v = float(input('Digite um valor real qualquer: '))
print(f'A porção inteira do número {v} é {trunc(v)}.')