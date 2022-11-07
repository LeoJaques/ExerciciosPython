frase = str(input('Digite uma frase: ')).strip().upper()
quant = frase.count('A')
a1 = frase.find('A')+1
ax = frase.rfind('A')+1
print('Quantas letras "A": {}'.format(quant))
print('A primeira letra "A" está na posição: {}'.format(a1))
print('A ultima letra "A" está na posição: {}'.format(ax))
