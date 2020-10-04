peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
massa = peso/ (altura**2)
print('Sua massa corporal é igual a {:.2f}!'.format(massa))
if massa < 18.5:
    print(' ')
    print('IMC abaixo de 18,5: Abaixo do Peso')
    
elif massa > 18.5 and massa <= 25:
    print(' ')
    print('Entre 18,5 e 25: Peso Ideal')
    
elif massa > 25 and massa <= 30:
    print(' ')
    print('25 até 30: Sobrepeso')
    
elif massa > 30 and massa <= 40:
    print(' ')
    print('30 até 40: Obesidade')
    
else:
    print(' ')
    print('Acima de 40: Obesidade Mórbida!')