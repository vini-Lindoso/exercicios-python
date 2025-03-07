print("-" * 40)
print(f"{'BANCO CEV':^40}")
print("-" * 40)

valor = int(input("Qual valor deseja sacar: R$"))
total = valor
céd = 50
totced = 0

while True:
    if total >= céd:
        total -= céd	
        totced += 1
    else:
        print(f"Total de {totced} cédulas de R${céd}")
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totced = 0
        if total == 0:
            break
                