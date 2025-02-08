'''m_abaixo = imc < 17
abaixo = imc >= 17 and imc < 18.5
ideal = imc >= 18.5 and imc < 25
sob = imc >= 25.5 and imc < 29.9
obe = imc >= 30.0 and imc < 34.9
obes = imc >= 35.0 and imc < 39.9
obem = imc >= 40'''

peso = float(input('Qual o seu peso: '))
alt = float(input('qual sua altura: '))
imc = peso / (alt ** 2)
if imc < 17:
    situ = 'muito abaixo'
if imc >= 17 and imc < 18.5:
    situ = 'abaixo'
if imc >= 18.5 and imc < 25:
    situ = 'ideal'
if imc >= 25.5 and imc < 29.9:
    situ = 'acima'
if imc >= 30.0 and imc < 34.9:
    situ = 'obesidade'
if imc >= 35.0 and imc < 39.9:
    situ = 'obesidade severa'
if imc >= 40:
    situ = 'obesidade morbida'
print('imc {:.2f}, seu peso é considerado {}'.format(imc,situ))