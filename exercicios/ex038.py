l = int(input('''Language / IdiomaPortugues
[1]Portugues
[2]English
opção: '''))
if l == 1 :
	n1 = int(input('Digite um numero inteiro: '))
	n2 = int(input('Digite outro numero inteiro: '))
	if n1 > n2:
		print('O primeiro valor é maior!\n{} > {}.'.format(n1, n2))
	elif n1 < n2:
		print('O segundo valor é maior!\n{} < {}.'.format(n1, n2))
	else:
		print('Não existe valor maior, os dois são iguais')
	print('fim!')
elif l == 2 :
	n1 = int(input('The first number:'))
	n2 = int(input('Second number: '))
	if n1 > n2:
		print('The first number is bigger!')
	elif n2 > n1:
		print('The second number is bigger')
	else:
		print('Both numbers are same!')
else:
	print('language unknown / idioma desconhecido.')