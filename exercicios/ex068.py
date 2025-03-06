from random import randint

resposta = numero = pori= computador = cont = 0

print("=-" * 20)
print("Vamos jogar par ou impar")
print("=-" * 20)

while True:
  numero = int(input("Digite um valor: "))
  pori = str(input("Par ou Impar?[P/I] ")).upper().strip()[0]
  while pori not in "PI":
    pori = str(input("Par ou Impar?[P/I] ")).upper().strip()[0]
  print("-" * 40)

  computador = randint(0,9)
  resultado = (computador + numero) % 2
  r = 0

  if resultado == 0:
    r = "P"
    resposta = "PAR"
  else:
    r = "I"
    resposta = "IMPAR"

  print(f"Você jogou {numero} e o computador {computador}. Total de {numero + computador} DEU {resposta}")

  if r == pori:
    print("Você ganho!")
    print("=-" * 20)
    cont += 1
  else:
    print("Você perdeu!")
    break

print("=-" * 20)
print(f'GAME OVER! Você venceu {cont} vezes')