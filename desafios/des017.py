#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import pow,sqrt,hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = sqrt(pow(co,2)+pow(ca,2))
print(f'O valor da hipotenusa é {h:.2f}.')
print(f'O valor da hipotenusa é {hypot(co,ca):.2f} (módulo).')