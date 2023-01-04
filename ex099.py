def maior(*n):
    if len(n) > 0:
        return print(max(n))

    return print('ERRO, insirar valores para iniciar o programa!')


maior(2, 9, 4, 5, 7, 1)
maior(7, 6, 2, 5)
maior(1)
maior()