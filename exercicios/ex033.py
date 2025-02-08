n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
n3 = int(input('digite o ultimo valor: '))
#VERIFICANDO QUEM É O MAIOR
if n1 > n2 and n1 > n3:
    maior = n1
else:
	if n2 > n3 and n2 > n1:
		maior = n2
	else:
		maior = n3
#VERIFICANDO QUEM É O MENOR
if n3 < n2 and n3 < n1:
	menor = n3
else:
	if n2 < n1 and n2 < n3:
		menor = n2
	else:
		menor = n1
print('O MAIOR valor digitado é {}\nO MENOR valor digitado é {}.'.format(maior, menor))