#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta de 3 níveis. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
turma = []
aluno = []
nota = []
r = 's'

while r == 's':
    aluno.append(str(input('Nome: ')))
    nota.append(float(input('Nota 01: ')))
    nota.append(float(input('Nota 02: ')))
    aluno.append(nota[:])
    media = (nota[0] + nota[1])/2
    aluno.append(media)
    turma.append(aluno[:])
    aluno.clear()
    nota.clear()
    r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

print(turma)