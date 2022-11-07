resp = 'S'
maior = menor = m = s = q = 0

while resp in 'Ss':
    núm = int(input('Digite um número: '))
    s += núm
    q += 1
    if q == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Continuar? [S/N] ')).upper().strip()[0]
m = s / q

print('Foram digitados {} números'.format(q))
print('A média entre eles é {:.2f}'.format(m))
print('O maior número foi o {} e o menor foi {}'.format(maior, menor))
