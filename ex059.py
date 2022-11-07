from time import sleep
menu = 0
print('=-'*15)
print('Digite dois valores')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('CARREGANDO MENU...')
while menu != 5:
    sleep(2)
    print('=-'*15)
    print('''Escolha uma das opções: 
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    menu = int(input('Digite sua escolha: '))
    if menu == 1:
        print('=-' * 15)
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('=-' * 15)
        print('O produto entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif menu == 3:
        print('=-' * 15)
        if n1 > n2:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
    elif menu == 4:
        print('=-' * 15)
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        print('CARREGANDO MENU...')
    elif menu == 5:
        print('ENCERRANDO O PROGRAMA...')
        sleep(1)
    else:
        print('[ERRO] Opção invalida, Tente novamente!')
print('Fim do programa!!')