''' Seja um conjunto S = {a1,...an} com n atividade que pode ser executadas em um
mesmo local. Exemplo: palestra em um auditório. Para todo i = 1,..,n, a atividade
ai começa no instante si e termina no instante fi com 0 <si<fi.
Ploblema Seleção de Atividades: Contre em S um subconjuton de atividades mutuamente
compativeis que tenha tamanho máximo.'''

# Temos um espaco físico para eventos. Mediante uma grande demanda, em busca do maior lucro, queremos otimizar a locacao deste espaco, foi implementado o seguinte algoritmo guloso.
# Inicializando os horarios de inicio e termino dos eventos candidatos a serem realizados em nosso espaco fisico.
inicio = [1,3,0,5,3,5,6,8,8,2,12]
fim = [4,5,6,7,8,9,10,11,12,13,14] #ordençao crescente
i = 0
n = len(inicio)
A = [1]

for m in range(1, n):
    if inicio[m] >= fim[i]:
        A.append(m+1)
        i = m
        

print('As atividades que podem ser executadas, maximizando a quantidade de eventos ao mesmo instante no espaco fisico disponível são:', A)

    










