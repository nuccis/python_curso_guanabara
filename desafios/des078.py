#Faça um programa que leia 5 valores númericos e guarde-as em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
nums = []

for c in range(0, 5):
    nums.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = nums[c]
    elif nums[c] > maior:
        maior = nums[c]
    elif nums[c] < menor:
        menor = nums[c]

print(f'Lista digitada: {nums}')

print(f'O maior número digitado foi {maior} e apareceu nas seguintes posições: ', end='')
for i, n in enumerate(nums):
    if n == maior:
        print(i, end='..')

print(f'\nO menor número digitado foi {menor} e apareceu nas seguintes posições: ', end='')
for i, n in enumerate(nums):
    if n == menor:
        print(i, end='..')