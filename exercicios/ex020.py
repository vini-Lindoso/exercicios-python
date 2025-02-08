n1 = str(input('aluno um: '))
n2 = str(input('aluno dois: '))
n3 = str(input('aluno tres: '))
n4 = str(input('aluno quatro: '))
lista = [n1, n2, n3, n4]
import random
ordem = random.shuffle(lista)
print('a odem de apresentação será')
print(lista)