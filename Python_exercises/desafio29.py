num = float(input('Qual a sua velocidade? '))
n = (num - 80) * 7
if num > 80:
    print('Multado! Multa de R${}!!'.format(n))
else:
    print('Tenha um bom dia e dirija com segurança')