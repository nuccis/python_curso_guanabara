#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com os valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]

for linha in range(0, 3):
    for num in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor [{linha}][{num}]: ')))

for linha in range(0, 3):
    for num in range(0, 3):
        print(f'{matriz[linha][num]:^4}', end=' ')
    print()
