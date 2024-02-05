#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele
v = input('Digite qualquer coisa: ')
print(f'Tipo primitivo: {type(v)}\n')
print(f'É alphanumerico: {v.isalnum()}\n'
        f'É alfabeto: {v.isalpha()}\n'
        f'É numérico: {v.isnumeric()}\n'
        f'É decimal: {v.isdecimal()}\n')
