#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar. (35 anos de contribuição)

from datetime import date

ano_atual = date.today().year

pessoa = dict()

pessoa['Nome'] = str(input('Digite seu nome: '))
nasc = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nasc
pessoa['Idade'] = idade
cart_trab = int(input('Digite sua CTPS (caso não tenha digite 0): '))
if cart_trab != 0:
    pessoa['CTPS'] = cart_trab
    pessoa['Contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['Salario'] = float(input('Digite seu salário: '))
    pessoa['Aposentadoria'] = (pessoa['Contratacao'] + 35) - nasc

print(pessoa)

for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')