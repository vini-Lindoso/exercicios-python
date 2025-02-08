
cont = int(input("numero:"))
s = cont
f = 1
r = 0
while cont > 0:
    print(s, " x ", cont, "  = ", f)
    f = f * cont
    cont -= 1


print(f)
