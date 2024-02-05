#Faça um programa que ajude um jogador de megasena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números de 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

bolao = list()


n = int(input('Digite a quantidade de jogos desejada: '))

for c in range(0, n):
    jogo = [randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60), randint(1,60)]
    bolao.append(jogo[:])
    jogo.clear()
    print(f'Jogo nº {c+1}: {bolao[c]}')

print(f'Todos os jogos: {bolao}')

