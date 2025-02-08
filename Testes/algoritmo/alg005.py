# Calculo do imc ( mass / altura²
# ideal  entre 18.5 e 25
massa = float(input('Quanto você pesa em kg:'))
altura = float(input('Qual a sua altura em Metros: '))
imc = massa / (altura ** 2)
if imc >= 18.5 and imc < 25.0:
    situ = 'ideal, Parabens!!'
else:
    situ = 'fora da normalidade'
print('Seu IMC é {:.1f} e este percentual é considerado {}'.format(imc , situ))