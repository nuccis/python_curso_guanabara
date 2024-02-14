#Funções
def resumo(v, acres=0, desc=0):
    print('-'*35)
    print('RESUMO DO VALOR'.center(35))
    print('-'*35)
    print(f'Preço analisado: \t{moeda(v)}')
    print(f'Dobro do preço: \t{dobro(v, formatar=True)}')
    print(f'Metade do preço: \t{metade(v, formatar=True)}')
    print(f'{acres}% de aumento: \t{aumentar(v, acres, formatar=True)}')
    print(f'{desc}% de redução: \t{diminuir(v, desc, formatar=True)}')

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