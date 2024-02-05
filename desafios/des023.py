#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#minha resolução:
nums = int(input('Digite um número entre 0 e 9999: '))
mi = nums//1000
nums = nums-mi*1000
cent = nums//100
nums = nums-cent*100
dez = nums//10
unid = nums - dez*10
print(f'Milhar: {mi:^5}')
print(f'Centena: {cent:^3}')
print(f'Dezenda: {dez:^3}')
print(f'Unidade: {unid:^3}')
#resolução do guanabara:
nums = int(input('Digite um número entre 0 e 9999: '))
unid = nums // 1 % 10
dez = nums // 10 % 10
cent = nums // 100 % 10
mi = nums // 1000 % 10
print(f'Milhar: {mi:^5}')
print(f'Centena: {cent:^3}')
print(f'Dezenda: {dez:^3}')
print(f'Unidade: {unid:^3}')