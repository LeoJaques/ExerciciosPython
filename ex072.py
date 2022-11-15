num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
       'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
       'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove'
       ,'Vinte')
while True:

    num_user = int(input('Digite um número entre 0 e 20: '))

    if 0 <= num_user <= 20:
        print(f'Você digitou o número {num[num_user]}')
    else:
        print('Tente novamente! Insira um número entre 0 e 20')
    continui = ' '
    while continui not in 'SN':
        continui = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continui == 'N':
        break
print('Fim do Programa')