#Faça um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo de fatorial.

#Funções
def fatorial(num, show=False):
    fat = 1
    print(f'Fatorial de {num}: ',end='')
    if show == True:
        while num >= 1:
            if num != 1:
                print(num, end=' X ')
                fat *= num
            else:
                print(f'{num} = ', end='')
            num -= 1
        
    else:
        while num >= 1:
            fat *= num
            num -= 1
    return fat

#Programa principal
print(fatorial(3, True))
print(fatorial(3))