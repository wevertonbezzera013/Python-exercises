from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} e tem {} em {}.'.format(ano, idade, atual))
if idade < 18:
    ida1 = 18 - idade
    print('Você só poderá se alistar daqui a {} ano(s)'.format(ida1))
    saldo = atual + ida1
    print('Seu alistamento será em {}.')
elif idade == 18:
    print('Você precisa se alistar imediatamente!!!')
elif idade > 18:
    ida2 = idade - 18
    print('Você precisava se alistar a {} ano(s) atrás.'.format(ida2))
    saldo = atual - ida2
    print('Seu alistamento foi em {}.')