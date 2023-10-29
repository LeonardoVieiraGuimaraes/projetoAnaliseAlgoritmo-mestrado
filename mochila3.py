'''Problema da Mochia Fracionária: Sendo uma mochia que admite um certo peso,
temos um conjutno de objetos, cada um com um valor e um peso. O objetivo é
selecionar o conjunto de objetos que caibam dentro da mochia de forma a
maximar o seu valor total dentro da mochila sendo que posso fracionar o objeto'''

capacidade = 30
valor = [300, 100, 400, 600, 840] #valor /peso [10, 10, 20, 20, 21] em ordem descrecente#
peso = [30, 10, 20, 30, 40]
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
    
