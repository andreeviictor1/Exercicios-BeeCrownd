valores = []  # Lista para armazenar valores positivos

for i in range(6):
    valor = float(input())
    if valor > 0:
        valores.append(valor)

positivos = len(valores)  # Quantidade de valores positivos
media_positivos = sum(valores) / positivos if positivos > 0 else 0

print(positivos, "valores positivos")
print(f"{media_positivos:.1f}")
