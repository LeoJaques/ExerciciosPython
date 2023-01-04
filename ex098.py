from time import sleep


def enfeite(q):
    print('-=' * q)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} passando {passo}')
    if fim < inicio:
        passo = -abs(passo)
        fim -= 1
    else:
        fim += 1
    enfeite(30)
    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = abs(int(input('Passo: ')))

contador(i, f, p)