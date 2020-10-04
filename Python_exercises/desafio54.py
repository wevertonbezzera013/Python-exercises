from datetime import date
atual = date.today().year
for c in range(1, 8):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = atual - ano
    if idade >= 21:
       print('{} pessoas atingiram a maior idade.'.format(c))
    else:
        print('{} pessoas são menores de idade.'.format(c))