import moeda

p = float(input('Digite o preço: R$ '))
print(f'Aumentando 10%, temos R$ {moeda.formating_monetary_values(moeda.aumentar(p, 10))}')
print(f'Diminuindo 20%, temos R$ {moeda.formating_monetary_values(moeda.diminuir(p, 20))}')
print(f'O dobro de R$ {moeda.formating_monetary_values(p)} é  R$ {moeda.formating_monetary_values(moeda.dobro(p))}')
print(f'A metade de R$ {p:.2f} é R$ {moeda.formating_monetary_values(moeda.metade(p))}')