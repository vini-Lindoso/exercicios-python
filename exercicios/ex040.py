idioma = int(input('[1]PORTUGUES [2]ENGLISH :'))
if idioma == 1:
	nota1 = float(input('Digite a sua primeira nota: '))
	nota2 = float(input('Digite a sua segunda nota: '))
	media = (nota1 + nota2)/2
	print('Sua media é {:.1f}'.format(media))
	if media >= 7 and media <= 10:
		print('Você está \033[1;32mAPROVADO\033[m')
	elif media < 5 and media > 0:
		print('Você está \033[1;31mREPROVADO\033[m')
	elif media > 5 and media < 6.99:
		print('Voce está de \033[1;33mRECUPERAÇÃO\033[m')
	else:
		print('Erro! Essa média não existe, nota minima 0 e maxima 10')
elif idioma == 2:
	nota1 = float(input('Type your first grade:'))
	nota2 = float(input('type your second grade:'))
	media = (nota1 + nota2) / 2
	print('Your avarage is {:.2f}'.format(media))
	if media >= 7 and media <= 10:
		print('You are \033[1;32mAPPROVED\033[m')
	elif media < 5 and media > 0:
		print('You are \033[1;31mREPPROVED\033[m')
	elif media > 5 and  media < 7:
		print('You are \033[1;33mRECOVERY\033[m')
	else:
		print('Error! This avarage does not exist, minimun avarege is 0 and a maximun avarage is 10')
else:
	print('Language Unknown! / Idioma desconhecido!')