contador = -1
soma = 0
numero = 0
while numero != 999:
    contador +=1
    soma += numero
    numero = int(input("Digite um numero[999 para parar]: "))
print("Você digitou {} e a soma entre eles foi {}." .format(contador, soma))

