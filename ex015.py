dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos KM você percorreu? '))
tot = (dias * 60) + (km * 0.15)
print('O preço a pagar por {} dias e {} Km é R${:.2f}'.format(dias, km, tot))
