while True:
  valor = int(input("quer ver a tabuada de qual valor?"))
  print("-" * 30)
  if valor < 0:
    break
  for cont in range(1,11):
    print(f"{valor} x {cont} = {cont*valor}")
  print('-' *30)
print("PROGRAMA DE TABUADA ENCERRADO. Volte sempre!")