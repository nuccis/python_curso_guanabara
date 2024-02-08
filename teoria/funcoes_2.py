#No python existe um ajuda interativa que pode ser acessada através da função interna help()
'''help(print)'''

#Podemos criar docstrings automáticas (depois de ter instalado a extensão) abrindo e fechando aspas 3 vezes e apertando enter

def contador(i:int, f:int, p:int) -> None:
    """Faz uma contagem e mostra na tela

    Args:
        i (int): Início da contagem
        f (int): Fim da contagem
        p (int): Passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c+=p
    print('FIM!')

contador(1,10,2)
'''help(contador)'''

#Parâmetros opcionais

def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(1,2)
somar(1, 3, 4)

#Escopo da variável
#As variáveis podem ser globais ou locais

def teste():
    x = 8 # x é uma variável local, só existe dentro da função teste
    print(f'Na função teste a variável x vale {x}.')
    print(f'Na função teste a variável n vale {n}.')

#Programa principal
n = 2 # n é uma variável global
print(f'No programa principal a variável n vale {n}.')
teste()

#Olhar o restante da explicação sobre escopo de variável nas imagens no celular.

#Funcionalidade return

def rsomar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = rsomar(3, 2, 5)
r2 = rsomar(1, 2)
r3 = rsomar(4, 7)

print(f'As respostas foram: {r1, r2, r3}')
