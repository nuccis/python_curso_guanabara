#des109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

n = float(input('Digite um Preço: R$'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, formatar=True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, formatar=True)}')
print(f'Aumentando 13% de {moeda.moeda(n)} fica: {moeda.aumentar(n, 13, formatar=True)}')
print(f'Diminuir 10% de {moeda.moeda(n)} fica: {moeda.diminuir(n, 10, formatar=True)}')