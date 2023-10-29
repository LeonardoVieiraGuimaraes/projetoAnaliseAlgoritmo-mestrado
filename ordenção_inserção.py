import random
import time
from pylab import*
import numpy

# A = random.sample(range(1, 50), 10)
k = 100
tempo = list()
elemento = list()

for p in range(20):
    A = list(range(k))
    #A.sort(reverse=True)
    inicio = time.time()

    for j in range(1,len(A)):
        chave = A[j]

        i = j - 1
        while i >= 0 and A[i] > chave:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = chave


    fim = time.time()
    t = fim-inicio
    k = k + 100
    tempo.append(t)
    elemento.append(k)
    

print(sum(tempo)/20)

plot(tempo)
xlabel('n')
ylabel('f(n)')
title('Complexidade de Tempo - Decrescente - Pior Caso')
show()
