#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Casa', 'Verde', 'Telhado', 'Rosa', 'Bota', 'Lua', 'Vermelho', 'Gato', 'Azul')
print('\n'+'-'*30)
for p in palavras:
    print(f'\nNa palavra {p} temos',end=' ')
    
    for l in ('a', 'e', 'i','o','u'):
        if l in p.lower():
            print(l,end=' ')

print('\n'+'-'*30)
for p in palavras:
    print(f'\nNa palavra {p} temos',end=' ')
    for l in p:
        if l.lower() in ('aeiou'):
            print(l,end=' ')