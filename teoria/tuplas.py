lanche = ('lanche', 'suco', 'pizza', 'pudim')
print(lanche[2])
print(lanche[0:2])
print(lanche[1:])
print(len(lanche))
print(lanche[-3])
for c in lanche:
    print(f'Eu vou comer {c}')
#Tuplas são imutáveis. Não dá para mudar as tuplas enquanto o programa estiver rodando.
print('Comi para caramba!')
for count in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[count]}')
print('Comi para caramba!')
for i, c in enumerate(lanche):
    print(f'{i+1}º eu vou comer {c}')
print('Comi para caramba!')
print(sorted(lanche))#A função sorted coloca os elementos em ordem e os salva em uma lista nova, não alterando a variável composta original
#--------------
a = (2, 5, 4)
b = (5, 8, 1, 2)
print(f'a = {a}')
print(f'b = {b}')
c = a + b #concatenação
print(f'c = {c}')
print(c.count(5))#Conta quantos 5 tem dentro de c
print(c.index(5))#mostra a posição da primeira ocorrencia do elemento 5
print(c.index(5, 2))#mostra a posição da primeira ocorrencia do elemento 5,a partir do 2º elemento da tupla
del(c)#deleta a tupla c, a partir de agora se formos fazer qlqr coisa com c, não dará certo, pois ela não existe mais
#print(c)