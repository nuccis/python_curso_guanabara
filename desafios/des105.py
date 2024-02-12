#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas, a maior nota, a menor nota, a média da turma e a situação (opcional).
#Adicione também as docstrings da função.

#funções
def notas(*args, sit=False):
    """Função para calcular as notas e a situação de um aluno

    Args:
        args (float): notas dos alunos
        sit (bool, optional): situação das notas do aluno. Defaults to False.

    Returns:
        _dict_: retorna um dicionário com as notas gerais do aluno e a situação, caso o parâmetro sit for True.
    """
    aluno = dict()
    s = 0
    for i, e in enumerate(args):
        if i == 0:
            maior = e
            menor = e
        elif e > maior:
            maior = e
        elif e < menor:
            menor = e
        s += e
    aluno['Quantidade'] = len(args)
    aluno['Maior_nota'] = maior
    aluno['Menor_nota'] = menor
    aluno['Media'] = s/len(args)
    if sit:
        if aluno['Media'] <= 5:
            aluno['Situacao'] = 'Ruim'
        elif aluno['Media'] > 5 and aluno['Media'] <= 7:
            aluno['Situacao'] = 'Boa'
        else:
            aluno['Situacao'] = 'Excelente'
    return aluno

#Programa principal
print(notas(8, 10, 8, 3, sit=True))