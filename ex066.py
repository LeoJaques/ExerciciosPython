
contador = soma = 0
while True:
    n = int(input('Digite um número; [PARA SAIR - 999]:' ))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Foram digitados {contador} números, e a soma entre eles é {soma}')
#já havia feito, while True para ter um loop infinito