nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2)/2
print('Sua média foi {:.2f}'.format(media))
if media <=6:
    print('Meu parcero, vc é um merda!')
else:
    print('Boa seu bosta!')