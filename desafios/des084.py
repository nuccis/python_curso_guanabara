#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas; B) Uma listagem com as pessoas mais pesadas; C) Uma listagem com as pessoas mais leves.

dados = list()
pessoas = list()
r = 's'

while r == 's':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if not pessoas:
        maior = dados[1]
        menor = dados [1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

print(f'Pessoas cadastradas: {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'Pessoas com o maior peso ({maior}): ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0],end='...')

print(f'\nPessoas com o menor peso ({menor}): ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0],end='...')