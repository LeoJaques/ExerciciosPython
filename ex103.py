def ficha(player='<desconhecido>', goal=0):
    print(f'O jogador {player} fez {goal} gol(s) no campeonato.')


n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(goal=g)
else:
    ficha(n, g)