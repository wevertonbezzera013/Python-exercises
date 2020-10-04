s = str(input('Digite seu sexo: ')).strip().upper()[0]
while s not in 'MmFm':
        s = str(input('Esse comando não é reconhecido no sistema, digite seu sexo [M/F]: ')).strip().upper()[0]
if s == 'M':
    print('Seu sexo é MASCULINO!')
elif s == 'F':
    print('Seu sexo é FEMININO!')