from tkinter import *

soma = quant = 0
while True:
  num = int(input("Digite um número (999 para parar):"))
  if num == 999:
    break
  soma += num
  quant += 1
print(f" A soma dos {quant} valores foi {soma}!")

janela = Tk()
janela.title("soma dos numeros digitados")

texto_orientaçao = Label(janela, text="Digite um número (999 para parar):")
texto_orientaçao.grid(column=0, row=0)

texto_orientaçao2 = Label(janela, text="teste:")
texto_orientaçao2.grid(column=0, row=1)

janela.mainloop()
