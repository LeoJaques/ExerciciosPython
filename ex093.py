jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, tot):
    partidas.append(int(input(f'  Quantos gol na partida {i + 1}? ')))
jogador['gols'] = partidas[:]
jogador['saldo'] = sum(partidas)
print(jogador)
print('='*40)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('='*40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for k, v in enumerate(jogador['gols'], 1):
    print(f'  => Na {k}° partida, fez {v} gols')
print(f'Foi um total de {jogador["saldo"]} gols')

