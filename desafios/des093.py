#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Partidas'] = int(input('Número de partidas: '))
gols = list()

for p in range(0, jogador['Partidas']):
    gols.append(int(input(f'Quantos gols na partida {p+1}: ')))

jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas')
for i, g in enumerate(jogador['Gols']):
    print(f'    => Na partida {i+1}, fez {g} gols')
print(f'Foi um total de {jogador["Total"]} gols')