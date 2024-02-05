#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*30)

c = 0

while True:
    n_player = int(input('Diga um valor: '))
    r = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    n_maq = randint(0, 10)
    resultado = (n_player + n_maq) % 2
    #print(n_maq)
    if (resultado == 0 and r == 'P') or (resultado != 0 and r == 'I'):
        print('Você venceu!\nVamos jogar novamente')
        print('-='*30)
        c += 1
    else:
        print('Você perdeu! Mais sorte na próxima!')
        break

print('-='*30)
print(f'Game Over! Você venceu {c} vez(es)')    