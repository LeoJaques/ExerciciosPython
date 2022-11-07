cidade = str(input('Qual o nome da sua cidade? ')).upper().strip()
div = cidade.split()
resposta = 'SANTO' in div[0]
print('O nome da cidade começa com SANTO: {}'.format(resposta))