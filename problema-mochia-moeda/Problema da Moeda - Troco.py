'''' Ploblema do Troco: Suponha que tenhamos disponíveis valores conforme
apresentados no vetor de moedas. O poblema e criar um algoritmo que para
conseguir obeter um determinado valor com o menor número de moedas possíveis'''

#Define as moedas disponiveis em ordem descrecente e troco desejado#
moedas = [100, 50, 20, 10, 5 , 2, 1] 
troco = int(input('Digite o troco desejado:'))                             
i = 0
n = len(moedas) #Tamanho do vetor de moedas#
total = 0;
if troco ==0:
    print('Não tem troco')

for i in range(n):
    num_moedas = troco//moedas[i] 
    troco -= num_moedas*moedas[i] 
    total += num_moedas
    if num_moedas != 0:
        print('%d de %d' %(num_moedas, moedas[i]))
    
print('Temos num total de %d moedas' %total)

'Tempo de Complexidade O(n)'



