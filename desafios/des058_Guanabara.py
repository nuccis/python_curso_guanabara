#des058: Melhore o jogo do Desafio 028 onde o computador vai ‘pensar’ em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('==O jogo vai começar==')
sleep(1)
print('Você deve adivinhar o número que eu estou pensando.')
sleep(1)
print('Este número está entre 0 e 10.')
sleep(1)

n = randint(0,10)
acertou = False
n_palp = 0

while not acertou:
    palp = int(input('Digite seu palpite: '))
    n_palp += 1
    if palp == n:
        acertou = True
    else:
        print('Você errou! Tente novamente.')

print('Parabéns, você acertou!')
print(f'Foram necessários {n_palp} palpite(s).')