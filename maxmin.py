
import time

from pylab import*


# A = random.sample(range(1, 50), 10)
k = 1000
tempo = list()
elemento = list()

for p in range(200):
    A = list(range(k))
    #pma = max(A)
    #pmi = min(A)
    #a = argmax(A)
    #b = argmin(A)
    #A[a] = A[0]
    #A[b] = A[1]
    #A[0] = pma
    #A[1] = pmi
    #list.reverse(A)


    inicio = time.time()
    maximo = A[0];
    minimo = A[0];
    for i in range(len(A)):
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

print(sum(tempo)/200)
plot(tempo)
xlabel('n')
ylabel('f(n)')
title('Complexidade de Tempo - Decrescente - Pior Caso')
show()

