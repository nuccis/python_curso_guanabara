#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que nenhum dado tenha sido informado corretamente.

def ficha(gol, jogador='<desconhecido>'):
    return f'O jogador {jogador} fez {gol} gol(s) no campeonato'

#Programa principal
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Quantidade de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome == '':
    print(ficha(gol=gols))
else:
    print(ficha(nome, gols))