lista_par = list()
lista_impar = list()
lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for v, i in enumerate(lista):
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print('-'*30)
print(f'A lista completa: {lista}')
print(f'A lista de ímpares:{lista_impar}')
print(f'A lista de pares: {lista_par}')

