'''Exercício Python 65:
Crie um programa que leia vários números inteiros
pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.'''

resposta = "s"
n = 0
menor = 0
maior = 0
media = 0
contador = 0
resposta = str(input("Quer digitar um numero[s/n]: "))
while resposta == "s":
    contador += 1
    n = int(input("Digite o número: "))
    media = (media + n) / contador
    if maior < n or maior == 0:
        maior = n
    elif menor > n or menor == 0:
        menor = n
    resposta = str(input("Quer digitar um numero[s/n]: "))
print("Você digitou {} numero\nA média é {}\nO maior número foi {}\nO menor número é {}".format(contador,media, maior, menor))
