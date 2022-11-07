print('=-=-=-=-Sequência de Fibonacci=-=-=-=-')
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    c += 1
    t1 = t2
    t2 = t3
print(' -> FIM DO PROGRAMA')