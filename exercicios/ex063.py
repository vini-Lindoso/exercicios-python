'''Exercício Python 63:
Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. '''
cenario = "-------------------------------------------"
print("{} \nSEQUENCIA DE FIBONNACCI\n{}".format(cenario, cenario))
numFib = int(input("Quantos numeros de fibonacci deseja ver:"))
cont = 1
n = 0
n1 = 1
print("Os {} primeiros numeros da sequencia de fibbonacci são:\n{}\n{}".format(numFib, cenario, n), end="")
while numFib != cont:
    cont += 1
    print(", {}".format(n1), end="")
    prov = n
    n = n1
    n1 += prov
print('\n{}' .format(cenario))

