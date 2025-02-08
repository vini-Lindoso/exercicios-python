nome = str(input('\033[1;34mQual é seu nome? '))
if nome == 'Vinicius':
	print('Que nome bonito!')
elif nome == 'Lucas'  or nome == 'João' or nome == 'Jose' or nome == 'Pedro':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Rosangela Maria Claudia Marta':
    print('Nossa que belo nome feminino')
else:
	print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))