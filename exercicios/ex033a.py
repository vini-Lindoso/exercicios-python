a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
lista = [a, b, c]
lista2 = sorted(lista)
print('O maior numero digitado foi {}\nO menor numero digitado foi {}'.format(lista2[2], lista2[0]))
