import random
import time


#A = random.sample(range(1, 50), 10)

A = range(100000)
A = list(A)
A.sort(reverse=True)



print(A)

inicio = time.time()
temp = A[0]
for i in range(1,len(A)):
    if temp<A[i]:
        temp = A[i]



print(temp)
fim = time.time()

print(fim-inicio)
