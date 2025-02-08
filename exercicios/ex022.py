nome = str(input('Seu nome completo: ')).strip()
print('seu nome em letras maiusculas é', nome.upper())
print('seu nome em letras minusculas é {}'.format(nome.lower()))
n1 = nome.replace(' ', '')
print('seu numero possui {} letras'.format(len(n1)))
lista = nome.split()
print('seu primeiro nome é', lista[0])
print('Seu primeiro nome possui {} letras'.format(len(lista[0])))



