n1 = float(input('qual a sua nota em portugues: '))
n2 = float(input('qual a sua nota em matematica: '))
m = (n1 + n2) / 2
print('a sua media é {:.1f}'.format(m))
if m >= 5:
    print('Sua nota foi boa, PARABENS!!')
else:
    print('Sua nota foi ruim, ESTUDA VAGABUNDO!!')