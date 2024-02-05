#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A"; Em que posição ela aparece pela primeira vez; Em que posição ela aparece a última vez;
frase = input('Digite uma frase: ').strip()
print(f'Quantas vezes aparece a letra "A": {frase.upper().count("A")}')
print(f'A posição que ela aparece pela primeira vez: {frase.upper().find("A")}')
print(f'A posição que ela aparece a última vez: {frase.upper().rfind("A")}') #com o modificador r ele começa da direita para a esquerda