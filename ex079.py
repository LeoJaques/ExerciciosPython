num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
    else:
        print('VALORES DUPLICADOS NÃO SÃO PERMITIDOS!!!')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-'*30)
num.sort()
print(f'Assim ficou a lista: {num}')