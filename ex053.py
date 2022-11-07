# frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
# print(frase)

frase = str(input('Digite uma frase:  ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]


# for i in range(len(junto) - 1, -1, -1):
#     inverso += junto[i]
print('{} = {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palídromo!')