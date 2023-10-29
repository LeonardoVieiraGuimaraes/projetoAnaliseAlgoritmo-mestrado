# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 01:07:17 2017

@author: Leonardo
"""

def trocomin(moedas, troco):
    total = 0
    i = 0
    n = len(moedas)

    if troco ==0:
        print('Não tem troco')

    for i in range(n):
        num_moedas = troco//moedas[i]
        troco -= num_moedas*moedas[i]
        total += num_moedas
        if num_moedas != 0:
            print('%d de %d' %(num_moedas, moedas[i]))
    
    print('Temos num total de %d moedas' %total)


moedas = []
moedas = [100, 50, 20, 10, 5 , 2, 1]
troco = 373
print (moedas)
trocomin(moedas, troco)
