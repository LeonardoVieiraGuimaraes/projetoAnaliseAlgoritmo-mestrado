moedas = (100, 50, 20, 10, 5 , 2, 1)
print (moedas)
total = 0
troco = 130
i = 0
n = len(moedas)

for i in range(n):
    num_moedas = troco //moedas[i]
    troco -= num_moedas*moedas[i]
    total += num_moedas

print(total)
