'''transformação de strings'''
frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android'))

'''deixa MAIUSCULO'''
print(frase.upper())

'''deixa minusculo'''
print(frase.lower())

'''Apenas primeira letra do texto em maiuscula'''
print(frase.capitalize())

'''Primeira letra de cada palavra em maiusculo'''
print(frase.title())

'''retira espaços vazios no final e inicio do texto'''
frase2 = '    Aprenda Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
