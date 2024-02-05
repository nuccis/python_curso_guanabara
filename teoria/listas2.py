#Parte 02
#Dessa maneira eu estou aninhando uma lista dentro da outra
pessoas = []
dados = ['Pedro', 25]
pessoas.append(dados[:]) #copia através de fatiamento p n criar link entre listas
print(f'Pessoas: {pessoas}')

pessoas2 = [['Pedro',25], ['Maria',19], ['João',32]]
print(f'Pessoas2: {pessoas2}')
print(f'índice [0][0]: {pessoas2[0][0]}')
print(f'índice [1][1]: {pessoas2[1][1]}')
print(f'índice [2][0]: {pessoas2[2][0]}')

for p in pessoas2:
    print(f'{p[0]} tem {p[1]} anos.')

galera = list()
dados1 = list()
for c in range(0,3):
    dados1.append(str(input('Digite o nome: ')))
    dados1.append(int(input('Digite a idade: ')))
    galera.append(dados1[:])
    dados1.clear()
print(galera)

