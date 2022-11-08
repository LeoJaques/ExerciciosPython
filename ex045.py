import random
from ast import Break
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
maq = random.randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
player = int(input('Qual é a sua jogada? '))
if player < 0 or player >= 3:
    print('(ERROR!). Opção invalida, tente novamente!')
    break
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print('-=' * 11)
    print('O computador escolheu {}.'.format(itens[maq]))
    print('Jogador escolheu {}'.format(itens[player]))
    print('-=' * 11)
    if maq == 0:
        if player == 0:
            print('EMPATE!')
        elif player == 1:
            print('PARABÉNS!! Você venceu.')
        elif player == 2:
            print('O computador venceu essa. Tente novamente!')
    elif maq == 1:
        if player == 0:
            print('O computador venceu essa. Tente novamente!')
        elif player == 1:
            print('EMPATE!')
        elif player == 2:
            print('PARABÉNS!! Você venceu!')
    elif maq == 2:
        if player == 0:
            print('PARABÉNS!! Você venceu!')
        elif player == 1:
            print('O computador venceu essa. Tente novamente!')
        elif player == 2:
            print('EMPATE!')




# falta as condições // 8:16