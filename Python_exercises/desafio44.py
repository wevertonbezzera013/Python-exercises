valor = float(input('Digite o valor do produto: R$'))
print(' ')
print('''Digite \033[0;32mD\033[m se você deseja pagar
à vista dinheiro/cheque: 10% de desconto!
Digite \033[0;32mE\033[m se você deseja pagar
à vista no cartão: 5% de desconto!
Digite \033[0;32mF\033[m se você deseja pagar
em até 2x no cartão: preço formal!
Digite \033[0;32mG\033[m se você deseja pagar
3x ou mais no cartão: 20% de juros!''')
print(' ')
op = str(input('Digite em quantas vezes você deseja pagar:'))
print(' ')
if op == 'D' or 'd':
    total = valor - (valor * 10/100)
    
elif op == 'E' or 'e':
    total = valor (valor * 5/100)
    
elif op == 'F' or 'f':
    total = valor
    parcela = tota/2
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))

elif op == 'G' or 'g':
    total = valor + (valor * 20/100)
    tp = int(input('Quantas parcelas? '))
    parcela = total/tp
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(tp, parcela))

else:
    total = 0
    print('Erro!')
print('O preço do produto vai de R${:.2f} para R${:.2f}'.format(valor, total))