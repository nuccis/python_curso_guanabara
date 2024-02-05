#Crie um programa que leia o nome completo de uma pessoa e mostre:O nome completo com todas as letras maiúsculas; O nome completo com todas as letras minúsculas; Quantas letras ao todo (sem considerar espaços); Quantas letras tem o primeiro nome.
nome = input('Digite seu nome completo: ').strip()
print(f'Nome maiúsculo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')
print(f'Quantidade de letras: {len(nome.replace(" ",""))}') 
#print(f'Quantidade de letras: {len(nome)-nome.count(" ")}') #Solução do Guanabara
separado = nome.split()
print(f'Quantidade de letras do primeiro nome: {len(separado[0])}')
#print(f'Quantidade de letras do primeiro nome: {nome.find(" ")}') #Solução do Guanabara
