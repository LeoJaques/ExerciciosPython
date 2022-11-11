mais_de_1000 = tot_gasto = menor_preco = cont = 0
produto_barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    tot_gasto += preco
    if preco > 1000:
        mais_de_1000 += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        produto_barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot_gasto:.2f}')
print(f'Temos {mais_de_1000} produtos que custaram mais de mil reais.')
print(f'O produto mais barato foi {produto_barato} que custa R$ {menor_preco:.2f} ')