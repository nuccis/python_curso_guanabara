#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) A média de idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média.

r = 's'
pessoa = dict()
grupo = list()

while r == 's':
    pessoa['nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: '))
    pessoa['Idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())

    r = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    while r not in 'sn':
        print('Opção incorreta!')
        r = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]

print(grupo)
print('-='*30)
print(f'foram cadastradas {len(grupo)} pessoas')