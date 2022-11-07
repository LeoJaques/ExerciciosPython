import datetime
salario = float(input('Qual o salário do colaborador? R$'))

if salario > 1250:
    print('O novo salário será de {:.2f}'.format(salario + (salario * 10 / 100)))
else:
    print('O novo salário será de {:.2f}'.format(salario + (salario * 10 / 100)))

