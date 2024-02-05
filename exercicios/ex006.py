#Estrutura de repetição com quantidade de repetição definida
'''c = 1
while c < 10:
    print(c)
    c+=1
print('FIM')'''

#Estrutura de repetição sem quantidade de repetição definida
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

r = 'S'
while r =='S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
print('Fim')