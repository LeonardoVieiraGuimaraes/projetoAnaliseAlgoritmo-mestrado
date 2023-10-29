import time
from pylab import*


# A = random.sample(range(1, 50), 10)
k = 1000
tempo = list()
elemento = list()

for p in range(200):
    A = list(range(k))
    #list.reverse(A)

    inicio = time.time()
    maximo = A[0]
    minimo = A[0]
    for i in range(1,len(A)):
        if A[i] > maximo:
            maximo  = A[i]
        elif A[i] < minimo:
            minimo = A[i]
    print(maximo)
    print(minimo)
    fim = time.time()
    t = fim-inicio
    k = k + 1000
    tempo.append(t)
    elemento.append(k)

print(sum(tempo)/200)
plot(tempo)
xlabel('n')
ylabel('f(n)')
title('Complexidade de Tempo - Decrescente - Pior Caso')
show()


