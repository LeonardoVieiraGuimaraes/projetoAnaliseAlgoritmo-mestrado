import time
import numpy
from pylab import*


def Merge(A,p,q,r):
    
    B = [0]*(r+1)
    for i in range(p,(q+1)):
        B[i] = A[i]
    for j in range(q+1,(r+1)):
        B[r+q+1-j] = A[j]  

    i = p
    j = r

    for k in range(p,r+1):
        if B[i] <= B[j]:
            A[k] = B[i]
            print(A[k],B[i])
            i = i+1
        else:
            A[k] = B[j]
            print(A[k],B[j])
            j = j-1


def Merge_Sort(A,p,r):
    if(p < r):
        q = int((p+r)/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        Merge(A,p,q,r)

         

l = 5
tempo = list()
elemento = list()
for i in range(1):
    V = list(range(l))
    
    p = 0
    r = len(V)-1
    list.reverse(V)
    print(V);
    inicio = time.time()
    Merge_Sort(V,p,r)
    fim = time.time()
    t = fim-inicio

    tempo.append(t)
    elemento.append(l)
    l = l + 1000
    
print(V);
print(p)
print(sum(tempo)/100)
plot(elemento, tempo)
xlabel('n')
ylabel('F(n)')
title('Complexidade de Tempo')
show()

