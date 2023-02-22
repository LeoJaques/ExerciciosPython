def per_cent_transform(num):
    return num / 100


def aumentar(num, per_cent):
    return  num + (num * per_cent_transform(per_cent))


def diminuir(num, per_cent):
    return num - ( num * per_cent_transform(per_cent))
    
    
def dobro(num):
    return num * 2
    
    
def metade(num):
    return num / 2