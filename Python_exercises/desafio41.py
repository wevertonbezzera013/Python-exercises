from datetime import date
ano = int(input('Digite sua idade: '))
atual = date.today().year
idade = atual - ano
print('Sua idade é {}!'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM!')
    
elif idade <= 14:
    print('Sua categoria é INFANTIL!')
    
elif idade <= 19:
    print('Sua categoria é JÚNIOR!')
    
elif idade <= 25:
    print('Sua categoria é SÊNIOR!')
    
else:
    print('Sua categoria é MASTER!')