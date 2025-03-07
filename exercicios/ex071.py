print("=-" * 20)
print(f"{'BANCO CEV':^40}")
print("=-" * 20)

valor = int(input("Qual valor deseja sacar: R$"))

notas = [100, 50, 20, 10, 5, 2, 1]
nota = notas[0]
cont = 0
while True:
    quantidade = valor // nota
    if quantidade == 0:
        cont += 1
        nota = notas[cont]
        continue
    valor = valor % nota
    print(f"Você receberá {quantidade} notas de R${nota:.2f}")
    if valor == 0:
        break
    cont += 1
    nota = notas[cont]
print("=-" * 20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
print("=-" * 20)
    