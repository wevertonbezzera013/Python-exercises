pa = str(input('Digite uma palavra: ')).strip()
pm = pa.lower()
pi = pm[::-1]
if pi == pm:
    print('Sim!')
else:
    print('Não!')