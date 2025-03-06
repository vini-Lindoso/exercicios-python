contador_de_maior = contador_de_homens = contador_mulher_menor = 0

while True:
    print(f"{'-=' * 20}\n {"Cadastre uma pessoa":^40}\n{'-=' * 20}")
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]")).upper().strip()[0]
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F]")).upper().strip()[0]
    if idade >= 18:
        contador_de_maior += 1
    if sexo == "M":
        contador_de_homens += 1
    if sexo == "F" and idade < 20:
        contador_mulher_menor += 1 
    print("-=" * 20)  
    continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if continuar == "N":
        break
print(f"Temos {contador_de_maior} pessoa(s) maiores de idade")
print(f"Temos {contador_de_homens} homem(ns) cadastrados")
print(f"Temos {contador_mulher_menor} mulher(es) com menos de 20 anos")
    