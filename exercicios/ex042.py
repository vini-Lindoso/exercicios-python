print('\033[1;30;47m-=-' * 17,'\033[m')
r1 = float(input('\033[47;30m{:>44}'.format('Digite o comprimento da primeira reta: ')))
r2 = float(input('\033[47;30m{:>44}'.format('Digite o comprimento da primeira reta: ')))
r3 = float(input('\033[47;30m{:>44}'.format('Digite o comprimento da terceira reta: ')))
lista = [r1 , r2 , r3]
ordem = sorted(lista)
print('\033[1;30;47m-=-' * 17,'\033[m')
print('Com retas de comprimentos de {:.0f}, {:.0f} e {:.0f}.'.format(r1, r2, r3))
if ordem[2] < ordem[0] + ordem[1]:
	if ordem[0] == ordem[1] and ordem[0] == ordem[2]:
		tipo = 'EQUILATERO'
	elif ordem[0] != ordem[1] and ordem[1] != ordem[2] and ordem[2] != ordem[0]:
		tipo = 'ESCALENO'
	else:
		tipo = 'ISOCELES'
	print('\033[1;32mÉ possivel\033[m formar um triangulo \033[1;34m{}\033[m'.format(tipo))
else:
	print('\033[1;31mNão é possivel\033[m formar um triangulo')