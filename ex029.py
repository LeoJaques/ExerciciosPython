print('-------Calcule o valor da multa-------')
vel = float(input('Qual a velocidade do veículo? Km/H '))
multa = (vel - 80) * 7
if vel <= 80:
    print('Não houve infração')
else:
    print('Houve infração e o valor da multa será de R$ {:.2f}'.format(multa))
print('Fim do programa')