from random import randrange
print('-------Jogo de advinhação-------')
print('')
cont = randrange(1, 5)
numero = int(input('Escolha um número de 1 á 5: '))
if cont == numero:
    print('Você acertou a máquina escolheu {} tambem'.format(cont))
else:
    print('Você errou, a máquina escolheu {} e você {}'.format(cont, numero))
print('')
print('-------Fim do jogo da advinhação-------')