
n = contador = soma = 0
while n != 999:
    n = int(input('Digite um número; [PARA SAIR - 999]:' ))
    if n == 999:
        break
    else:
        contador += 1
        soma += n
print('Foram digitados {} números, e a soma entre eles é {}'.format(contador, soma))