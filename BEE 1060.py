contagem_positivos = 0


for i in range(6):
    valor = float(input("Digite um valor: "))
    
    if valor > 0:
        contagem_positivos += 1


print(f'{contagem_positivos} valores positivos')
