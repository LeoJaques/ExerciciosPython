def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro, insira somente números inteiros\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mPrograma finalizado pelo usuário.\033[m')
        else:
            return num


