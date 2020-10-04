salario = float(input('Digite seu salário: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Salário com aumento de 15% é igual a R${:.2f}'.format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Salário com aumento de 10% R${:.2f}'.format(novo))