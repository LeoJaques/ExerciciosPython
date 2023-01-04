def area(l, c):
    tot = l * c
    print(f'A área de um terreno {l}x{c} é de {tot}m²')


larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(larg, comp)