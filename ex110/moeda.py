def per_cent_transform(num=0):
    resp = num / 100
    return resp 


def aumentar(num=0, per_cent=0, formato=False):
    resp = num + (num * per_cent_transform(per_cent))
    return resp if formato is False else formating_monetary_values(resp)


def diminuir(num=0, per_cent=0, formato=False):
    resp = num - ( num * per_cent_transform(per_cent))
    return resp if formato is False else formating_monetary_values(resp)

      
def dobro(num=0, formato=False):
    resp = num * 2   
    return resp if formato is False else formating_monetary_values(resp)

    
def metade(num=0, formato=False):
    resp = num / 2
    return resp if formato is False else formating_monetary_values(resp)


def formating_monetary_values( price = 0, coin = 'R$'):
    return f'{coin} {price:.2f}'.replace('.', ',')
    
def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{formating_monetary_values(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de desconto: \t{diminuir(preco, taxar, True)}')
    print('-'*30)
