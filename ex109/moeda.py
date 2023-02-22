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
    