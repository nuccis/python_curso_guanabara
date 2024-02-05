#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite a tabuada que deseja: '))
    if n < 0:
        print('-'*50)
        print('O PROGRAMA DE TABUADA ESTÁ SENDO ENCERRADO.\nATÉ A PRÓXIMA!')
        print('-'*50)
        break
    print('-'*50)
    print(f'TABUADA DO NÚMERO {n}')
    print('-'*50)
    for i in range(0, 11):
        print(f'{n} x {i} = {n*i}')

    