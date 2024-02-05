#Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores digitados; B) A soma dos valores da terceira coluna; C) O maior valor da segunda linha.

matriz = [[], [], []]
somaTotal = 0
soma3coluna = 0
maior2coluna = 0
somapar = 0

for linha in range(0, 3):
    for col in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor [{linha+1}][{col+1}]: ')))
        somaTotal += matriz[linha][col]
        if matriz[linha][col] % 2 == 0:
            somapar += matriz[linha][col]
        if col == 2:
            soma3coluna += matriz[linha][col]
        if linha == 1 and matriz[linha][col] > maior2coluna:
            maior2coluna = matriz[linha][col]

print('Matriz:')
for linha in range(0, 3):
    for col in range(0, 3):
        print(f'{matriz[linha][col]:^4}', end=' ')        
    print()

print(f'A soma de todos os valores: {somaTotal}')
print(f'A soma de todos os pares: {somapar}')
print(f'A soma dos valores da 3º coluna: {soma3coluna}')
print(f'O maior valor da 2º linha: {maior2coluna}')
