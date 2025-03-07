mais_barato = total = cont = 0
nome_mais_barato = ""

print(f"{40*'-'}\n{'LOJA SUPER BARTÃO':^40}\n{40*'-'}")
while True:
    produto = str(input("Nome do Produto:")).strip().title()
    preco = float(input("Preço: R$"))
    if preco >= 1000:
        cont += 1
    if mais_barato > preco or mais_barato == 0:
        mais_barato = preco
        nome_mais_barato = produto
    total += preco
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if continuar == "N":
        break
print(f"{40*'-'}\n{'Fim do Programa':^40}\n{40*'-'}")  
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {cont} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nome_mais_barato} que custa R${mais_barato:.2f}")
