num = int(input('Digite um número de 0 a 9999: '))
n = str(num)
un = n[3]
de = n[2]
cen = n[1]
mil = n[0]
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(un, de, cen, mil))