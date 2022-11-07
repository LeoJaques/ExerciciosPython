from math import hypot
catop = float(input('Qual o comprimento do cateto oposto: '))
catad = float(input('Qual o comprimento do cateto adjacente: '))
print('O valor da hiptenusa é {:.2f}'.format(hypot(catop, catad)))
