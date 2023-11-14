cod, qnt = input().split()
cod = int(cod)
qnt = int(qnt)

if(cod == 1):
    total = qnt * 4
elif(cod == 2):
    total = qnt * 4.50
elif(cod == 3):
    total = qnt * 5
elif(cod == 4):
    total = qnt * 2
elif(cod == 5):
    total = qnt * 1.5

print("Total: R$ %.2f" %total)



# produtos = cachorro quente, x-salada, x-bacon, torrada simples, refrigerante 
# preco = 4, 4.50, 5, 2, 1.5 