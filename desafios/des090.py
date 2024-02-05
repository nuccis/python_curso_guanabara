#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = int(input('Média: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'reprovado'
else:
    aluno['Situação'] = 'aprovado'

print(f'O nome do aluno é {aluno["Nome"]}')
print(f'E sua situação é {aluno["Situação"]}')