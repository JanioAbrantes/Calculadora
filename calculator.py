"""
Uma simples calculadora
"""
from decimal import Decimal
logo = """
 _____________________
|  _________________  |
| | Pythonista   1.0| |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
print('Caso deseje fechar a calculadora, deixe a expressão em branco e aperte ENTER')
print('Para usar essa calculadora, digite o primeiro número, a operação e o segundo número. Ex: 10 + 1.5')


def soma(x, y):
    return Decimal(x + y)

def subtracao(x, y):
    return Decimal(x - y)

def multiplicacao(x, y):
    return Decimal(x * y)

def divisao(x, y):
    return Decimal(x / y)

def calcular(x=0):
    valor_guardado = x
    try:
        if x == 0:
            operacao = input('Digite a expressão a ser calculada: ').replace(' ', '')
        else:
            operacao = input(f'Digite a expressão a ser calculada: {x} ').replace(' ', '')

        if '+' in operacao:
            operador = '+'
            operacao = operacao.split('+')
            if x == 0:
                resultado = soma(Decimal(operacao[0]), Decimal(operacao[1]))
            else:
                operacao[0] = x
                resultado = soma(Decimal(operacao[0]), Decimal(operacao[1]))
        elif '-' in operacao:
            operador = '-'
            operacao = operacao.split('-')
            if x == 0:
                resultado = subtracao(Decimal(operacao[0]), Decimal(operacao[1]))
            else:
                operacao[0] = x
                resultado = subtracao(Decimal(operacao[0]), Decimal(operacao[1]))
        elif '*' in operacao:
            operador = '*'
            operacao = operacao.split('*')
            if x == 0:
                resultado = multiplicacao(Decimal(operacao[0]), Decimal(operacao[1]))
            else:
                operacao[0] = x
                resultado = multiplicacao(Decimal(operacao[0]), Decimal(operacao[1]))
        elif '/' in operacao:
            operador = '/'
            operacao = operacao.split('/')
            if x == 0:
                resultado = divisao(Decimal(operacao[0]), Decimal(operacao[1]))
            else:
                operacao[0] = x
                resultado = divisao(Decimal(operacao[0]), Decimal(operacao[1]))
        else:
            print('Operação Inválida')
            calcular(valor_guardado)

    except:
        print('Operação Inválida')
        calcular()

    print(f'O resultado da operação {(Decimal(operacao[0]))} {operador} {Decimal(operacao[1])} é: {resultado}')
    continua = input('Deseja continuar a operar com o resultado? digite Y para sim: ').upper()
    if continua == 'Y':
        calcular(resultado)
    else:
        calcular()


calcular()
