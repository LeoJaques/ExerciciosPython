print('{}Bradesco Financiamento{}'.format('\033[1;30;41m', '\033[m'))
print('{}Informe os dados abaixo para simular seu financiamento:{}'.format('\033[7;40m', '\033[m'))

casa = float(input('Qual o valor da casa?\nR$ '))
salario = float(input('Qual o seu sálario?\nR$ '))
anos = int(input('Em quantos anos você quer pagar a casa?\n'))
prestacao = casa / (anos * 12)
corte = salario * (30 / 100)


if (prestacao <= corte):
    print('{}PARABENS!!! FINACIAMENTO APROVADO!!{}'.format('\033[1;30;42m', '\033[m'))
else:
    print('{}FINACIAMENTO NEGADO!!{}'.format('\033[1;30;41m', '\033[m'))