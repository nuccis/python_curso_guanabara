#Os erros levantados quando se compila um código, que não sejam erro sintático, são chamados de exceção
#Para fazer o tratamento dessas exceções utilizamos a estrutura: try...except...
#As cláusulas else e finally são opcionais. Sendo que o else acontece caso o que foi posto no try funcione, e o finally acontece independente se o que foi posto no try funcione ou não. 
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema :(')
else:
    print(f'A divisão entre {a} e {b} é {r}')
finally:
    print('Volte sempre. Muito Obrigada!')

#Podemos utilizar também a subclasse Exception para mostrar o erro:
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'A divisão entre {a} e {b} é {r}')
finally:
    print('Volte sempre. Muito Obrigada!')

#É uma boa prática ser o mais específico possível com os tipos de exceções que pretendemos manipular, para isso podemos utilizar vários except
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dado digitados.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'A divisão entre {a} e {b} é {r}')
finally:
    print('Volte sempre. Muito Obrigada!')