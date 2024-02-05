#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
v1 = float(input('Insira a largura da parede: '))
v2 = float(input('Insira a altura da parede: '))
print(f'Você irá precisar de {(v1*v2)/2:.2f} litros de tinta.')