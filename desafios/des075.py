#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o número 9; B) Em qual posição foi digitado o primeiro número 3; C) Quais foram os números pares?

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o primeiro número: '))
n3 = int(input('Digite o primeiro número: '))
n4 = int(input('Digite o primeiro número: '))

nums = (n1, n2, n3, n4)

print(f'A tupla gerada {nums}')
print(f'O número 9 apareceu {nums.count(9)} vez(es)')

if 3 in nums:
    print(f'O número 3 apareceu pela primeira vez na posição {nums.index(3)+1}')
else:
    print('O número 3 não apareceu em nenhuma posição')

print('Os números pares digitados foram: ',end='')
for n in nums:
    if n%2 == 0:
        print(n,end=' ')

