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

v1 = [0, 1, 0, 4, 0 , 0, 0]
v2 = [1, 0, 2, 6, 4 , 0, 0]
v3 = [0, 2, 0, 0, 5 , 6, 0]
v4 = [4, 6, 0, 0, 3 , 0, 0]
v5 = [0, 4, 5, 0, 0 , 8, 0]
v6 = [0, 0, 6, 0, 8 , 0, 0]
v7 = [0, 0, 0, 4, 7 , 3, 0]

V = [v1,v2,v3,v4,v5,v6,v7]
dist = []

E = [[0,1],[1,2],[3,4],[5,6],[0,3],[1,4],[3,6],[2,4],[1,3],[2,5],[4,6],[4,5]] 
r = 2
n = 7
adj = []
for u in range(0,n):
     dist.append(10000)

dist[r] = 0;

Q = []

for v in range(0,n):
    Q.insert(0,v)
    print(Q)
while Q!=[]:
    u = min(Q)
    Q.remove(u)
    for v in range(0,n):
        if V[u] != 0:
            adj.insert(u,V[u])
            print(adj[u])
    if dist[u] + V[u][v] < dist[v]:
        
        
            
