'''Problema da Mochia Fracionária: Sendo uma mochia que admite um certo peso,
temos um conjutno de objetos, cada um com um valor e um peso. O objetivo é
selecionar o conjunto de objetos que caibam dentro da mochia de forma a
macimar o valor total dentro da mochila'''

capacidade = 50
valor = [60, 100, 120] #valor / peso [6, 5, 4] em ordem descrecente#
peso = [10, 20, 30]
n = len(valor)
x = [0]*n 


for j in range(n-1,-1,-1):
    if peso[j] <= capacidade:
        x[j] = 1
        capacidade = capacidade - peso[j]
    else:
        x[j] = capacidade/peso[j]
        capacidade = 0

print(x)
    
