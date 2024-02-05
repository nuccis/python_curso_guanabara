print('Lanches:')
lanche = ['lanche', 'suco', 'pizza', 'pudim']
print(lanche)
#listas são mutáveis, logo eu posso substituir valores:
lanche[3] = 'picolé'
print(lanche)
#para adicionar elementos novos na lista. Esse item vai para o final da lista
lanche.append('cookie') 
print(lanche)
#para adicionar elementos em uma posição desejada utilizamos o seguinte método:
lanche.insert(2,'cachorro-quente')
print(lanche)
#para apagar elementos podemos fazer:
del lanche[3]
print(lanche)
lanche.pop(2)#se não passar nenhum índice ele remove o último item
print(lanche)
lanche.remove('lanche')
print(lanche)
#criar uma lista utilizando um range
print('valores:')
valores = list(range(4,11))#4 5 6 7 8 9 10 
print(valores)
#ordenar uma lista
valoresDois = [4, 9, 1, 7, 3]
print(valoresDois)
valoresDois.sort()#ordena a lista
print(valoresDois)
valoresDois.sort(reverse=True)#ordena de maneira inversa
print(valoresDois)
#saber o tamanho de uma lista
len(valoresDois)

#utilização de laços com listas
print('Laços:')
for v in valores:
    print(f'{v}...', end='')
print()
for i, v in enumerate(valores):
    print(f'Na posição {i} encontrei o valor {v}')
valoresTres = []
for count in range(0,3):
    valoresTres.append(int(input('Digite um número: ')))
print(valoresTres)

#link de listas
#quando igualamos uma lista a outra, criamos um link entre elas. Logo se eu mudar um item em uma lista, na outra acontecerá a mesma coisa
a = [2, 6, 4]
b = a
print(f'Lista a {a}')
print(f'Lista b {b}')
b[0] = 0
print(f'Lista a {a}')
print(f'Lista b {b}')

#criar uma cópia de uma lista
c = [2, 6, 4]
d = c[:]
print(f'Lista c {c}')
print(f'Lista d {d}')
d[0] = 0
print(f'Lista c {c}')
print(f'Lista d {d}')
