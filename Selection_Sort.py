# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:17:45 2017

@author: Leonardo
"""

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
    A.sort(reverse=True)
    n=len(A)
    inicio = time.time()
    for i in range(0,n-1):
        minimo = i
        for j in range(i+1,n):
            if A[j] < A[minimo]:
                minimo = j
        if A[i] != A[minimo]:
            temp = A[i]
            A[i] = A[minimo]
            A[minimo] = temp

    
    fim = time.time()
    t = fim-inicio
    k = k + 100
    tempo.append(t)
    elemento.append(k)


print(sum(tempo)/20)
plot(tempo)
xlabel('n')
ylabel('f(n)')
title('Complexidade de Tempo - Drescente - Pior Caso')

show()   