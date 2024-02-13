#Funções
def aumentar(v, t):
    return v * (1 + t/100)

def diminuir(v, t):
    return v * (1 - t/100)

def dobro(v):
    return v * 2

def metade(v):
    return v / 2

def moeda(v, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
