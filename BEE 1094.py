total_cobaias = 0 
total_coelhos = 0
total_ratos = 0
total_sapos = 0

N = int(input())

for i in range(N):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)
    
    if tipo == 'C':
        total_coelhos += quantidade
    elif tipo == 'R':
        total_ratos += quantidade 
    elif tipo == 'S':
        total_sapos += quantidade
        
    total_cobaias += quantidade
    
percentual_coelhos = (total_coelhos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_sapos = (total_sapos / total_cobaias) * 100


print("Total: %d cobaias" % total_cobaias)
print("Total de coelhos: %d" % total_coelhos)
print("Total de ratos: %d" % total_ratos)
print("Total de sapos: %d" % total_sapos)
print("Percentual de coelhos: %.2f %%" % percentual_coelhos)
print("Percentual de ratos: %.2f %%" % percentual_ratos)
print("Percentual de sapos: %.2f %%" % percentual_sapos)