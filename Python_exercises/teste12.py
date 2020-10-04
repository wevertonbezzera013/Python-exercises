nome = str(input('Digite seu nome: ')).strip()
if nome == 'Weverton':
    print('Que nome maneiro!')
elif nome == 'Ana' or nome == 'Pedro' or nome == 'Lucas':
    print('Seu nome é muito popular no Brasil, {}!'.format(nome))
else:
    print('Olá, {}! Prazer em te conhecer!'.format(nome))