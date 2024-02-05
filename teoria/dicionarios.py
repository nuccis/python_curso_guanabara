#Dicionários são identificados por {}
dados = dict()
dados = {'Nome': 'Pedro', 'idade':25}
print(dados)
print(dados['Nome'])
print(dados['idade'])

#Para adicionar elementos
dados['Sexo'] = 'Masculino'
print(dados)
del dados['idade']
print(dados)

#Dic para guardar filmes
print('\nFilmes:')
filme = {'Titulo': 'StarWars', 'Ano': '1977', 'Diretor': 'Jorge Lucas'}
print(filme)
#No python nos chamamos os elementos do dicionário de items, keys e values
print(filme.values())
print(filme.keys())
print(filme.items())

for key, value in filme.items():
    print(f'O {key} é {value}')

print('\nLocadora:')
#Podemos mesclar lista, com dicionário, com tupla...
locadora = [{'Titulo': 'StarWars', 'Ano': '1977', 'Diretor': 'George Lucas'}, {'Titulo': 'Avengers', 'Ano': '2012', 'Diretor': 'Joss Whedon'}, {'Titulo': 'Matrix', 'Ano': '1999', 'Diretor': 'Wachowski'}]

print(locadora[0]['Ano'])
print(locadora[2]['Titulo'])

#Estados
print('\nEstados:')
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'Mato Grosso', 'Sigla': 'MT'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['UF'])

estado = dict()
brasil2 = list()
for c in range(0, 3):
    estado['UF'] = str(input('Digite o nome do estado: '))
    estado['Sigla'] = str(input('Digite a sigla: '))
    brasil2.append(estado.copy())

print(brasil2)

for e in brasil2:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

for e in brasil2:
    for v in e.values():
        print(v, end=' ')
    print()


