#Crie um programa a onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente. 

r = 's'
nums = []

while r == 's':
    n = int(input('Digite um número: '))
    if n not in nums:
        nums.append(n)
        print('Número adicionado com sucesso')
    else:
        print('Este número já existe na lista.')
    r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

nums.sort()
print(f'Você digitou os seguinte números {nums}') 