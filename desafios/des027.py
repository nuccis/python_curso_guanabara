#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = input('Digite seu nome completo: ').strip()
separado = nome.split()
print(f'Nome completo: {nome}')
print(f'Primeiro nome: {separado[0]}')
print(f'Último nome: {separado[len(separado)-1]}')