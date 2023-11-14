pares = impares = positivos = negativos = 0

for _ in range(5):
    valor = int(input())
    
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

print(pares, "valor(es) par(es)")
print(impares, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")
