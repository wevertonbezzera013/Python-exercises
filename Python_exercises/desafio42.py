print('\033[0;31m =× \033[m' * 21)
print('\033[0;32m      _.:!ANALISADOR DE TRIÂNGULO!:._ \033[m')
print('\033[0;31m =× \033[m' * 21)
print(' ')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print(' ')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;32mOs segmentos acima podem\nformar triângulos! \033[m', end= ' ')
    print(' ')
    if r1 == r2 == r3:
        print(' ')
        print('Este triângulo é \033[0;34mEQUILÁTERO\033[m!')
        
    elif r1 != r2 != r3:
        print(' ')
        print('Este triângulo é \033[0;34mESCALENO\033[m!')
    else:
        print(' ')
        print('Este triângulo é \033[0;34mISÓSCELES\033[m!')

else:
    print(' ')
    print('\033[0;31mOs segmentos acima\nnão podem formar triângulos! \033[m')