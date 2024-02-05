#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente. No final, mostre o conteúdo das três listas gerados. Obs: utilizar laços diferentes para o processo

r = 's'
total = []
par = []
impar = []

while r == 's':
    n = int(input('Digite um número: '))
    total.append(n)
    r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

for e in total:
    if e % 2 == 0:
        par.append(e)
    else:
        impar.append(e)

print(f'Você digitou os seguintes números: {total}')
print(f'Lista de números pares: {par}')
print(f'Lista de números ímpares: {impar}')