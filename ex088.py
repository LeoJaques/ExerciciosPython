from random import randint
from time import sleep
lista = []
print('-'*30)
print('      JOGA NA MEGA SENA')
print('-'*30)
quant = int(input('Quantos jogos deseja sortear? '))

for i in range(1, quant + 1):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    print
    print(f'Jogo: {i} {lista}')
    sleep(1)
    lista.clear()
print('-'*30)
print('Boa sorte!')