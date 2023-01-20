def voto(nasc):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'

    return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print(voto(2007))
print(voto(2010))
print(voto(1999))





