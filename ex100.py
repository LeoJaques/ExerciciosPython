from random import randint
from time import sleep

def sorteia(lst):
    for i in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO')

def somaPar(lst):
    s = 0
    for i in lst:
        if i % 2 == 0:
            s += i
    print(f'A soma dos valores pares é {s}')

num = []

sorteia(num)
somaPar(num)

