'''O algoritmo de Prim encontra uma árvore geradora mínima para um grafo desde
que ele seja valorado e não direcionado.
Por exemplo, se na figura 1 os vértices deste grafo representassem cidades e
as arestas fossem estradas de terra que interligassem estas cidades, como
poderíamos determinar quais estradas asfaltar gastando a menor quantidade
de asfalto possível para interligar todas as cidades. O algoritmo de Prim
neste caso fornecerá uma resposta ótima para este problema que não
necessariamente é única. A etapa f) da figura 1 demonstra como estas cidades
devem ser conectadas com as arestas em negrito.'''

import numpy as np

#v1 = [0, 1, 0, 4, 0 , 0, 0]
#v2 = [1, 0, 2, 6, 4 , 0, 0]
#v3 = [0, 2, 0, 0, 5 , 6, 0]
#v4 = [4, 6, 0, 0, 3 , 0, 0]
#v5 = [0, 4, 5, 0, 0 , 8, 0]
#v6 = [0, 0, 6, 0, 8 , 0, 0]
#v7 = [0, 0, 0, 4, 7 , 3, 0]





A = []
C = []
E = [[0,1],[1,2],[3,4],[5,6],[0,3],[1,4],[3,6],[2,4],[1,3],[2,5],[4,6],[4,5]] 

n = 7
for v in range(0,n):
    C.append(v)
    print(C)

for i in range(0,n):
    x = E[i][0]
    y = E[i][1]
    cx = C[x]
    cy = C[y]
    if C[x] != C[y]:
        A.append([x,y])
        C.remove(cx)
        C.remove(cy)
        C.insert(cx,cx)
        C.insert(cy,cy)
       
        
        print(C)
    else:
        break


print(A)
        
    
