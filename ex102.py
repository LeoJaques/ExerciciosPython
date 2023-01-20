def fatorial(num, show=False):
    '''
    ->Calcula o Fatorial de um número
    :param num: Número que irá ser calculado
    :param show: Parâmetro para exibir o calculo
    :return: O resultado da operação
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(9, True))

help(fatorial)
