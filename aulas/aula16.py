# tuplas = variavel composta imutavel, sinalizada por () ou no novo python, até sem parenteses
# metodo len(0) retorna o tamanho da tupla
# metodo count() retorna a quantidade de vezes que um elemento aparece na tupla
# metodo index() retorna a posicao do elemento na tupla
# metodo sorted() pode ser usado para mostrar a tupla em ordem alfabetica ou crescente
# utilizamos o : para sinalizar que é de um item até outro, exemplo 1:3 (de um até três)
# podemos somar duas tuplas, quando fazemos isso, o resultado é uma tupla com todos os valores
# metodo del() pode ser usado para apagar uma variavel ou um tupla inteira, não pode ser usada em um elemento

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[0])    #PRIMEIRO ITEM
print(lanche[1])    #SEGUNDO ITEM
print(lanche[1:3])  #DO SEGUNDO AO TERCEIRO
print(lanche[2:])   #DO TERCEIRO EM DIANTE
print(lanche[:2])   #ATE O SEGUNDO
print(lanche[:2])   #FATIAMENTO DE TUPLAS
print(lanche[-1])   #ULTIMO
print(lanche[-2])   #PENULTIMO

print("-" * 40)
print(len(lanche))

for comida in lanche:
    print(f"Eu vou comer {comida}")
    
for cont in range(0, len(lanche)):
    print(f'{cont}///{lanche[cont]}')

for pos, alimento in enumerate(lanche):
    print(f'Eu vou comer {alimento} na posição {pos}')
    
a = (1,2,3,5)
b = (4,5,6,7)
c = a + b
print(c)
print(c.count(5))
print(c.index(2))