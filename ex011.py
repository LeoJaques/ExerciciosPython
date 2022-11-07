a = float(input('Qual a altura da parede?' ))
l = float(input('Qual a largura?'))
at = a * l
t = at / 2
print('Para pintar a parede com uma área de {}m² é necessario {} litros de tinta.'.format(at, t))