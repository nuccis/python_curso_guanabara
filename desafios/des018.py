#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.
from math import radians,sin,cos,tan
a = float(input('Digite um ângulo qualquer em graus: '))
ar = radians(a)
print(f'O seno de {a} é {sin(ar):.2f}')
print(f'O cosseno de {a} é {cos(ar):.2f}')
print(f'A tangente de {a} é {tan(ar):.2f}')