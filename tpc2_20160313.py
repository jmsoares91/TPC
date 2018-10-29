#SAD TPC2 João Soares 20160313 Informática de Gestão (PL)


import itertools

naipe = ['C','E','P','O']

valor = ['2','3','4','5','6','7','8','9','10','D','V','R','A']

temp = list(itertools.product(naipe, valor))

baralho = []

for i in range(0, len(temp)): 
        (a,b) = temp[i]
        baralho.append(a+b)
print(baralho)

A = ['P10','E9','C1','C1','O2','E9']

num_baralhos = 0

v = 0

while v < len(A):
	if A[v] in baralho: 
		baralho.remove(A[v])
		v += 1
	else:
		num_baralhos += 1
		v += 1
    

print("Num de baralhos necessarios: " + str(num_baralhos))

