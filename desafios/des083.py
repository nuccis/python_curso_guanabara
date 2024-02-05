#Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.

expr = str(input('Digite uma expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if pilha:
            pilha.pop()
        else:
            pilha.append(')')
            break

if not pilha:
    print('Sua expresão está válida!')
else:
    print('Sua expressão não está válida!')