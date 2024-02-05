#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados; B) A lista de valores ordenados de forma decrescente; C) Se o valor 5 foi digitado e está ou não na lista:

r = 's'
nums = []

while r == 's':
    n = int(input('Digite um número: '))
    nums.append(n)
    r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

print(f'Foram digitados {len(nums)} números')
nums.sort(reverse=True)
print(f'Ordenados inversamente {nums}')
if 5 in nums:
    print(f'O valor 5 foi digitado')
else:
    print(f'O valor 5 não foi digitado')