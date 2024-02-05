#Faça um programa que leia um número qualquer e mostre o seu fatorial

#fatorial com while
'''num = int(input('Digite um número: '))
fator = num
fatorial = 1

while num > 1:
    fatorial *= num
    num -= 1

print(f'O fatorial de {fator} é {fatorial}')'''

#fatorial com while personalizado
'''num = int(input('Digite um número: '))
fatorial = 1
print(f'{num}! =', end=' ')

while num > 0:
    if num == 1:
        print(f'{num}', end=' ')
    else:
        print(f'{num}', end=' x ')
    fatorial *= num
    num -= 1'''

#fatorial com while personalizado - Guanabara
num = int(input('Digite um número: '))
fatorial = 1
print(f'{num}! =', end=' ')

while num > 0:
    print(num, end='')
    print(' x ' if num > 1 else ' = ', end='' )
    fatorial *= num
    num -= 1


print(f'{fatorial}')

#fatorial com for
'''num = int(input('Digite um número: '))
fatorial = 1

for i in range(1, num+1):
    fatorial *=i
    
print(f'O fatorial de {num} é {fatorial}')'''

#fatorial com for personalizado
'''num = int(input('Digite um número: '))
fatorial = 1
print(f'{num}! =', end=' ')
for i in range(num, 0, -1):
    fatorial *=i
    if i == 1:
        print(f'{i}', end=' ')
    else:
        print(f'{i}', end='x')

print(f'= {fatorial}')'''