# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 23:20:59 2017

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
    #A.sort(reverse=True)
    inicio = time.time()
    n = len(A)
    trocado = True
    while trocado:
        trocado = False
        for j in range(n-1):
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                trocado = True
        
    
    fim = time.time()
    t = fim-inicio
    k = k + 100
    tempo.append(t)
    elemento.append(k)
print(sum(tempo)/20)
plot(tempo)
xlabel('n')
ylabel('f(n)')
title('Complexidade de Tempo - Crescente - Melho Caso')
show()
   