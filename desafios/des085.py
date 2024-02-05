#Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares em ordem crescente.
nums = [[], []]

for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)

print(f'Números digitados: {nums}')
nums[0].sort()
nums[1].sort()
print(f'Números digitados em ordem: {nums}')