#des107: Crie um módulo chamado moeda.py que tenha as funções incorporadas: aumentar(), diminuir(), dobro() e metade().
#Faça também um programa que importe esse módulo e use essas funções
#des108: Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como uma valor monetário formatado.

import moeda

n = float(input('Digite um Preço: R$'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'Aumentando 13% de {moeda.moeda(n)} fica: {moeda.moeda(moeda.aumentar(n, 13))}')
print(f'Diminuir 10% de {moeda.moeda(n)} fica: {moeda.moeda(moeda.diminuir(n, 10))}')