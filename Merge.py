def Merge(A,p,q,r):
    print(p,q,r)
    p = int(p)
    q = int(q)
    r = int(r)
    print(p,q,r)
    n1 = q-p+1
    n2 = r-q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(0, (n1)):
        L[i] = A[p+i-1]

    for j in range(0, (n2)):
        R[j] = A[q+j]

    L[n1] = 10000000
    R[n2] = 10000000

    j = 0
    i = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k-1] = L[i]
            i = i+1
        else:
            A[k-1] = R[j]
            j = j+1


def Merge_Sort(A,p,r):
    if(p < r):
        q = abs((p+r)/2)
        #q = int(q)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        Merge(A,p,q,r)




import random
A = random.sample(range(1, 101), 11)
print(A)
p = 1
r = len(A)
Merge_Sort(A,p,r)

print('\n',A)




