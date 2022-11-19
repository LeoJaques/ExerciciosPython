exp = str(input('Digite a expressão: '))
pilha = []
for i in exp:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está correta!!')
else:
    print('Sua expressão está incorreta!!')