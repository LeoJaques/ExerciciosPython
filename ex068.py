from random import randint

wins = 0
while True:
    player = int(input('Digite um valor: '))
    maq = randint(0, 10)
    tot = player + maq
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input(' Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {maq}. Total de {tot}')
    print(f'DEU PAR' if tot % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            print('-'*30)
            print('Você venceu!!!')
            wins += 1
        else:
            print('-'*30)
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('-'*30)
            print('Você venceu!!!')
            wins += 1
        else:
            print('-'*30)
            print('Você perdeu!!!')
            break
print(f'FIM DE JOGO! Você venceu {wins} vezes')
