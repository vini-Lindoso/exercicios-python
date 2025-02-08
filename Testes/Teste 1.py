l1 = int(input('digite o primeiro lado: '))
l2 = int(input('digite o segundo lado: '))
l3 = int(input('digite o segundo lado: '))

triangulo = l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2
equilatero = l1 == l2 and l2 == l3 and triangulo == True
escaleno = l1 != l2 and l2 != l3 and l1 != l3 and triangulo == True
isoceles = triangulo == True and equilatero == False and escaleno == False

print('pode formar um triangulo:', triangulo)
print('pode formar um triangulo equilatero:' , equilatero)
print('pode formar um triangulo escaleno:', escaleno)
print('pode formar um triangulo isoceles', isoceles)
