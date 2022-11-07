a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o segundo número:'))
maior = a
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi o {}.'.format(menor))
print('O maior valor digitado foi o {}.'.format(maior))