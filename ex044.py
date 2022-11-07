print('{:=^40}'.format('JAQUES ELETRO'))
preco = float(input('Qual o valor do produto? (R$) '))
print('''Qual será a forma de pagamento: 
[ 1 ] - à vista DINHEIRO/PIX
[ 2 ] - à vista no cartão DÉBITO/CRÉDITO
[ 3 ] - em 2x no cartão
[ 4 ] - em 3x ou mais no cartão''')
res = int(input('  Escolha uma das opções: '))
if res == 1:
    total = preco - (preco * 10 / 100)
    print(total)
elif res == 2:
    total = preco - (preco * 5 / 100)
    print(total)
elif res == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} COM JUROS'.format(parcela))
elif res == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    valor = total / parcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(parcelas, valor))
else:
    total = 0
    print('OPÇÃO INVALIDADE de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}.'.format(preco, total))