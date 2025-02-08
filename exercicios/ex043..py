peso = float(input('Qual seu peso atual: kg '))
altura = float(input('Qual a sua altura: cm '))
altura= altura / 100
imc = peso / (altura * altura)
print('Uma pessoa que pesa {:.1f}kg medindo {:.2f}mt terá um IMC de \033[1;34m{:.1f}'.format(peso, altura, imc))
if imc < 18.5:
	cond = '\033[1;31mAbaixo do Peso\033[m\nPode ser necessario procurar um especialista'
elif 18.5 <= imc < 25:
	cond = '\033[1;32mPeso Ideal, Parabens!'
elif 25 <= imc < 30:
	cond = '\033[1;33mSobrepeso\033[m\nPode ser necessario procurar um especialista'
elif 30 <= imc < 40:
	cond = '\033[1;31mObesidade\033[m\nProcure um especialista'
else:
	cond = '\033[1;31mObesidade Mórbida\033[m\nProcure urgentemente um especialista.'
print('E esse indice é classificado como {}'.format(cond))