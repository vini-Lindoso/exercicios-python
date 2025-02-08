n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('nome do terceiro aluno: '))
n4 = str(input('nome do quarto aluno: '))
lista = [n1 , n2, n3 , n4]
import random
r = random.choice(lista)
print('O aluno escolhido foi {} !'.format(r))


