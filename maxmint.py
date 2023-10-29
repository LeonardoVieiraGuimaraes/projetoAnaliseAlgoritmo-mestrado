import random
import time
from pylab import*
import numpy

# A = random.sample(range(1, 50), 10)
k = 1000
tempo = list()
elemento = list()

for p in range(200):
    A = list(range(k))
    A.sort(reverse=True)
    inicio = time.time()
    maximo = A[0];
    minimo = A[0];
        for i in range(1,len(A)):
            if A[i] > maximo:
                maximo  = A[i]
            if A[i] <minimo:
                minimo = A[i]

    fim = time.time()
    t = fim-inicio

    print(maximo)
    print(minimo)
    k = k + 1000

    tempo.append(t)
    elemento.append(k)
    
print(sum(tempo)/20)
plot(tempo)
xlabel('n')
ylabel('f(n)')
title('Complexidade de Tempo - Decrescente - Pior Caso')
show()



