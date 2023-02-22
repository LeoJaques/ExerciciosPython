def per_cent_transform(num=0):
    return num / 100


def aumentar(num=0, per_cent=0):
    return  num + (num * per_cent_transform(per_cent))


def diminuir(num=0, per_cent=0):
    return num - ( num * per_cent_transform(per_cent))
    
    
def dobro(num=0):
    return num * 2
    
    
def metade(num=0):
    return num / 2

def formating_monetary_values( price = 0, coin = 'R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')
    