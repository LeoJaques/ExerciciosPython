jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range(0, tot):
        partidas.append(int(input(f'  Quantos gol na partida {i + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['saldo'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Responda apenas S ou N')
    if resp == 'N':
        break
print('-'*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time, 1):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 encerrar) ')) - 1
    if busca == 998:
        break
    if busca > len(time) or busca < 0:
        print(f'ERROR! Não existe jogador com o código {busca + 1}')
        print('-'*40)
    else:
        print(f' -- LEVANTAMENDO DO JOGADOR {time[busca]["nome"]}')
        for k, v in enumerate(time[busca]['gols'], 1):
            print(f'     No jogo {k} fez {v} gols.')
            print('-'*40)