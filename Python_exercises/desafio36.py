casa = float(input('Digite o preço da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos você deseja pagar a casa: '))
num = casa/(anos * 12)
mínimo = salario * 30/100
print('Para pagar a casa em {} anos você precisará de R${:.2f} '.format(anos, num))
if num <= mínimo:
    print('Empréstimo pode ser concebido.')
else num > mínimo:
    print('Empréstimo negado.')