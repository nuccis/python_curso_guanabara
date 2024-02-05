#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
#Minha resolução
nome = input('Digite o nome de uma cidade: ').strip().upper()
nome = nome.split()
print(f'O nome da cidade começa com SANTO? {"SANTO" in nome[0]}')
#Resolução do guanabara
nome = input('Digite o nome de uma cidade: ').strip().upper()
print(f'O nome da cidade começa com SANTO? {nome[:5] == "SANTO"}')