#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas, a maior nota, a menor nota, a média da turma e a situação (opcional).
#Adicione também as docstrings da função.

def notas(*args, sit=False):
    aluno = dict()
    