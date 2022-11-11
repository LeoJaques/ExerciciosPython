print('='*30)
print('{:^30}'.format('Banco Dev'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula_atual = 50
tot_cadulas = 0
while True:
    if total >= cedula_atual:
        total -= cedula_atual
        tot_cadulas += 1
    else:
        if tot_cadulas > 0:
            print(f'Total de {tot_cadulas} cédulas de R${cedula_atual}')
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        tot_cadulas = 0
        if total == 0:
            break
print('Saque concluido!! O Banco Dev agradece!')

