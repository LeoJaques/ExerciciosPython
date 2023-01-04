def escreva(msg):
    
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))

while True:
    mensagem = str(input('Digite uma frase: '))
    if len(mensagem) > 0:
        break
    print('Por favor insirar um texto antes de continuar!')
    print('-'*40)
    



escreva(mensagem)


