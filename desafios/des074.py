#Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

conj = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os número sorteados foram: ',end='')

for ind, e in enumerate(conj):
    if ind == 0:
        maior = e
        menor = e
    elif e > maior:
        maior = e
    elif e < menor:
        menor = e
    print(e,end=' ')

print(f'\nO maior valor gerado foi {maior}')
print(f'O menor valor gerado foi {menor}')