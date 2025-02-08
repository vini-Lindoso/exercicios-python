'''Conta quantos caracteres tem na frase'''
frase = 'Curso em Video Python'
len(frase)
print(len(frase))

'''Conta quantas vezes um caracter aparece em uma frase'''
print(frase.count('o',0,14))

'''procura parte de um frase dentro de um texto'''
print(frase.find('deo'))

'''diz se o a string existe dentro de um texto'''
print('android' in frase)
print('em' in frase)