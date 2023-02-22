def leia_dinheiro(msg):
    enter = str(input(msg)).replace(',', '.').strip()
    try:
        return float(enter)
    except ValueError:
        print(f'\033[0;31mERRO: \"{enter}\" é um preço inválido!\33[m')
        return leia_dinheiro(msg)


