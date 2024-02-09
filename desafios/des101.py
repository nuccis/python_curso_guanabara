# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem o voto "Negado", "Opcional" ou "Obrigatório" nas eleições.
# maior que 65 anos: opcional
# entre 18 e 65 anos: obrigatóri
# menor que 18 anos: negado
# A função deve retornar uma frase

#Funções
def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade > 65:
        return f'A votação para uma pessoa de {idade} anos é opcional'
    elif idade < 18:
        return f'A votação para uma pessoa de {idade} anos não é permitida'
    else:
        return f'A votação para uma pessoa de {idade} é obrigatória'

#Programa principal
ano = int(input('Digite o seu ano de nascimento: '))
print(voto(ano))