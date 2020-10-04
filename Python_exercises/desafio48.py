soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 #contador
        soma = soma + c #acumulador
print('Existem {} números divisiveis por 3  a soma deles é {}!'.format(cont, soma))
print('Fim!')