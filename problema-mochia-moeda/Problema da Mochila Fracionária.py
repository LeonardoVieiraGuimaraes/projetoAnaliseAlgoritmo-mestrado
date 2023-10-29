'''Problema da Mochia Fracionária: Sendo uma mochia que admite um certo peso,
temos um conjutno de objetos, cada um com um valor e um peso. O objetivo é
selecionar o conjunto de objetos que caibam dentro da mochia de forma a
maximar o seu valor total dentro da mochila sendo que posso fracionar o objeto'''

capacidade = int(input('Digite a capacidade da mochila em kg:'))
valor = [300, 150, 400, 600, 1200] #valor /peso [10, 15, 20, 25, 30] em ordem crescente#
peso = [30, 10, 20, 24, 40]
n = len(valor)
bolsa = [0]*n 

for j in range(n-1,-1,-1): #Percorre as posicoes do vetor "valor" de forma decrescente#
    if peso[j] <= capacidade:
        bolsa[j] = 1
        capacidade = capacidade - peso[j]
    else:
        bolsa[j] = capacidade/peso[j]
        capacidade = 0

print(bolsa)
print('Capacidade restante na mochila apos otimizacao: %d kg' %capacidade)
    
