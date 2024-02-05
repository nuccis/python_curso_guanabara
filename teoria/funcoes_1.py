#Para criar um comando utilizamos def
def linha():
    print('-'*30)

linha()

#Podemos passar um parâmetro para as nossas funções
def msg(mens):
    print('-'*30)
    print(f'{mens:^30}')
    print('-'*30)

msg('olá todos')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(2, 3)

#Ordem de precedência dos parâmetros:
    # -> positional arguments, keywords arguments, *args(tuplas), **kwargs(dict)

#função com empacotamento em tuplas
def cont(*args):
    print(f'Eu recebi os valores {args}, sendo o total de {len(args)} elementos')

cont(1, 2, 3)
cont(5, 7)

#função com listas como parâmetros
#Obs: toda passagem de parâmetros do python é por referência
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos +=1
    
valores = [1, 2, 3]
dobra(valores)
print(valores)