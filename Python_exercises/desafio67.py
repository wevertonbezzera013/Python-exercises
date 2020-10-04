while True:
    n = int(input('Digite um valor: ')
    if n<0:
        break
    	
    for c in range(1, 11):
        print('{} × {} = {}'.format(c, n, c*n))
        	
print('Programa encerrado.')
