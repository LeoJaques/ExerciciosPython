print('''A SOMA ENTRES OS NÚMEROS IMPARES
QUE SÃO MÚLTIPLOS DE TRÊS ENTRE 1-500''')
soma = 0
for i in range(1, 500+1):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
print('A soma é: {}'.format(soma))