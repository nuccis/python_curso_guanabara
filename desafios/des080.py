#Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar sort()). No Final mostre a lista ordenada na tela

lista = []
lista.append

for n in range(0, 5):
    num = int(input('Digite um número: '))
    
    if not lista :
        lista.append(num)
        print('O número foi aidicionado ao final da lista...')
    else:
        pos = 0
        while True:
            if num < lista[pos]:
                lista.insert(pos, num)
                print(f'O número foi aidicionado na posição {pos} da lista...')
                break
            elif pos == len(lista) - 1:
                lista.append(num)
                print('O número foi aidicionado ao final da lista...')
                break
            pos+=1
            
print(f'Você digitou a seguinte lista {lista}')