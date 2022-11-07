from random import randint
from time import sleep
computador = randint(1, 10)
print('Olá sou seu computador... Acabei de pensar em um número entre 1-10')
print('Tente advinhar qual foi!!!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
      acertou = True
    else:
        if jogador < computador:
            print('MAIS! Tente mais uma vez!')
        else:
            print('MENOS! Tente mais uma vez!')
print('Acertou!!! Com {} tentativas'.format(palpites))
















# print('-------Jogo de advinhação-------')
# print('')
# cont = randint(1, 10)
# print('''Escolha um número entre 1-10:
# [ 0 ] Sair do programa''')
# numero = int(input('Digite sua escolha: '))
# tentativas = 0
# while numero != cont:
#     if cont == numero:
#         print('Você acertou a máquina escolheu {} tambem'.format(cont))
#         print('Foram {} tentativas até você acertar!'.format(tentativas))
#     elif numero == 0:
#         print('Encerrando programa...')
#         cont = numero
#         sleep(1)
#     else:
#         tentativas += 1
#         print('-='*10)
#         print('Você errou! A máquina não escolheu {}'.format(numero))
#         print('''Tente novamente! Digite um número entre 1-10:
# [ 0 ] Sair do programa''')
#
#
# print('')
# print('-------Fim do jogo da advinhação-------')