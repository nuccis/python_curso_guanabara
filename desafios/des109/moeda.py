#Funções
def aumentar(v, t, formatar = False):
    valor = v * (1 + t/100)
    if formatar:
        valor = moeda(valor)
    return valor

def diminuir(v, t, formatar = False):
    valor = v * (1 - t/100)
    if formatar:
        valor = moeda(valor)
    return valor

def dobro(v, formatar = False):
    valor = v * 2
    if formatar:
        valor = moeda(valor)
    return valor

def metade(v, formatar = False):
    valor = v / 2
    if formatar:
        valor = moeda(valor)
    return valor

def moeda(v, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')