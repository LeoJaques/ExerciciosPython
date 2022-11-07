print('TESTE DE NÚMEROS PRIMOS')
num = int(input('Digite um número: '))
tot = 0
for i in range (1, num + 1):
    if num % i == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{} '.format(i), end='')
print('\n\33[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')