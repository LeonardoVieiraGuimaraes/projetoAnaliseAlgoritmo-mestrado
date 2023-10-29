import time
from pylab import*


# A = random.sample(range(1, 50), 10)
k = 1000
tempo = list()
elemento = list()

for p in range(1):
    A = list(range(k))
    n = len(A)
    #list.reverse(A)
    
    inicio = time.time()
    
    if (n % 2) > 0:
        list.append(A,A[n-1])
        fimdoanel = (n-1)
    else:
        fimdoanel = (n-2)
    if A[0] > A[1]:
        maximo=A[0]
        minimo = A[1]
    else:
        maximo = A[1]
        minimo = A[0]
        
    i = 2
    while i <= fimdoanel:
        if A[i] > A[i+1]:
            if A[i] > maximo:
                maximo = A[i]
            if A[i+1] < minimo:
                minimo = A[i+1]
        else:
            if A[i] < minimo:
                minimo = A[i]
            if A[i+1] > maximo:
                maximo = A[i+1]
        i = i + 2
        
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


