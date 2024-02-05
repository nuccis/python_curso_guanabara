#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: [A] Quantas pessoas tem mais de 18 anos. [B] Quantos homens foram cadastrados. [C] Quantas mulheres tem menos de 20 anos.
cm = ch = cj = 0
while True:
    print('-='*30)
    print(f'{"CADASTRE UMA PESSOA":^60}')
    print('-='*30)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if sexo == 'F' and idade < 20:
        cm += 1
    if idade > 18:
        cj += 1
    if sexo == 'M':
        ch += 1
    
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break

print('-='*30)
print(f'{"PROGRAMA ENCERRADO":^60}')
print('-='*30)
print('Foram cadastrados: ')
print(f'Pessoas com mais de 18 anos: {cj}')
print(f'Mulheres com menos de 20 anos: {cm}')
print(f'Homens: {ch}')
