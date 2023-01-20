def leiaInt(msg):
    num = input(msg)
    if num.isnumeric():
        return num
    return leiaInt('\033[0;31mErro, insira somente números: \033[m')


n = leiaInt('Dígite um número: ')
print(f'O número digitado foi : {n}')