def mostrar_numero():
  teste = True
  while(teste):
    try:
      num = int(input('Digite um número menor que 100: '))
      if 100 > num > 0:
        print('Você digitou o número {}.'.format(num))
        teste = False
      else:
        print('\33[43;30mPOR FAVOR INSIRA UM VALOR MENOR QUE 100\33[m')
    except:
      print('\33[41;30m[ERRO FORMATO INSERIDO INVALIDO]\33[m')

print('Testador de números')
outro_teste = True

# try:
#   roda = str(input('Iniciar progromar? [S/N]')).strip().upper()
#   if roda == 'S':
#     mostrar_numero()
#   elif roda == 'N':
#     print('Obrigado por usar o programa!')
#   else:
#     print('\33[43;30mPOR FAVOR DIGITE "S" OU "N"\33[m')
# except:
#   print('\33[41;30m[ERRO FORMATO INSERIDO INVALIDO]\33[m')
