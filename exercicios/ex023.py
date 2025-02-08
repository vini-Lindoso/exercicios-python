numero = int(input('Digite um numero entre 0 e 9999: '))
m = int(numero/1000)
c = int((numero/100) - (m * 10))
d = int((numero/10) - (m * 100 + c * 10))
u = int(numero/1) - (m * 1000 + c * 100 + d * 10 )
print('Unidades = {} \nDezenas = {} \nCentenas = {} \nMilhar = {}'.format(u ,d ,c ,m))
print((1234/100) - (1234/1000 * 10))


