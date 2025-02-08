anon = int(input('Em que ano você nasceu? '))
houm = str(input('Genero MASCULINO ou FEMININO:')).strip()
if houm.upper() == 'MASCULINO':
	import datetime
	anoh = datetime.date.today().year
	idade = anoh - anon
	if idade > 18:
		print('Você tem {} e já passou o tempo de se alistar\n Seu alistamento deveria ser em {}'.format(idade, anon + 18))
	elif idade == 18:
		print('Você tem exatamente {} anos e está na hora de se alistar'.format(idade))
	elif idade < 18 and idade > 0:
		print('Você ainda não tem idade para se alistar. faltam {} anos, seu alistamento será em {}'.format(18-idade, anon + 18))
	else:
		print('Você ainda nem nasceu!')
elif houm.upper() == 'FEMININO':
	print('Você não necessita se alistar.')
else:
	print('Puxa não entendi.')