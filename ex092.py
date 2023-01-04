from datetime import datetime

dados = {}
ano_atual = datetime.now().year
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 - não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - ano_atual)

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')

