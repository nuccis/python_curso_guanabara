#Crie um programa onde 4 jogadores joguem um dado de 6 lados e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador01':randint(1,6), 'Jogador02':randint(1,6), 'Jogador03':randint(1,6), 'Jogador04':randint(1,6)}
ranking = list()

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(.25)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(f'\n{'RANKING':^25}')
for i, e in enumerate(ranking):
    print(f'{i+1}º lugar: {e[0]} com {e[1]}')
    sleep(.25)