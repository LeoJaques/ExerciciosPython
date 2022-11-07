km = float(input('Qual a a distância da viagem? Km '))
if km <= 200:
    print('O valor da passagem será: R$ {:.2f}'.format(km * 0.50))
else:
    print('O valor da passagem será: R$ {:.2f}'.format(km * 0.45))