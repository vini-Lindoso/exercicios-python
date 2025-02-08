'''funçoes de Divisão'''
''' divide a frase em outras frases'''
frase = 'Curso em Video, de Python'
print(frase.split())
print(frase.split(','))


'''Troca os espaços por um caractere desejado'''
frase2 = 'curso em video python'
lista = frase2.split()
print('-'.join(frase2))
print('-'.join(lista))
print(' . '.join(lista))




