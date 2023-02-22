import moeda


p = float(input('Digite o preço: R$ '))
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10, formato=True)}')
print(f'Diminuindo 20%, temos R$ {moeda.diminuir(p, 20, formato=True)}')
print(f'O dobro de R$ {moeda.formating_monetary_values(p)} é  R$ {moeda.dobro(p, formato=True)}')
print(f'A metade de R$ {moeda.formating_monetary_values(p)} é R$ {moeda.metade(p, formato=True)}')
