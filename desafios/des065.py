#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

c = 0 
soma = 0
r = 'S'

while r == 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    if c == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    c += 1
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

print('Os resultados foram:')
print(f'Média dos valores {soma/c}')
print(f'O maior valor: {maior}\nO menor valor: {menor}')