somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    
    print('='*20)
    print('   {}° PESSOA'.format(p))
    print('='*20)
    
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    Sexo = str(input('Sexo[M/F]: ')).strip().upper()
    
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    
mediaidade = idade / 4

print('A mé dia de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))