#des057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado peça a digitação novamente até ter o correto.

sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Opção inválida. Digite novamente.')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
print('Opção correta!')