#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('='*20)
print(f'A ordem de apresentação é:')
print(f'Primeira pessoa {lista[0]}')
print(f'Segunda pessoa {lista[1]}')
print(f'Terceira pessoa {lista[2]}')
print(f'Quarta pessoa {lista[3]}')