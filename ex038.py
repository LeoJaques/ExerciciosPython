num1 = int(input('{}Digite um número: {}'.format('\033[1;40m', '\033[m')))
num2 = int(input('{}Digite outro número: {}'.format('\033[7;40m', '\033[m')))

if num1 > num2:
    print('O número {}{}{} é maior que número {}{}{}.'.format('\033[1;40m', num1, '\033[m', '\033[7;40m', num2, '\033[m'))
elif num2 > num1:
    print('O número {}{}{} é maior que o número {}{}{}.'.format('\033[7;40m', num2, '\033[m', '\033[1;40m', num1, '\033[m'))
else:
    print('Os números {}{}{} e {}{}{} são iguais.'.format('\033[1;40m', num1, '\033[m', '\033[7;40m', num2, '\033[m'))
