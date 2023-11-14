valor = int(input())

print(valor)

# Lista de notas e contador de notas
notas = [100, 50, 20, 10, 5, 2, 1]
contador_notas = [0, 0, 0, 0, 0, 0, 0]

# Calcula a quantidade de notas de cada tipo necessárias
for i in range(7):
    contador_notas[i] = valor // notas[i]
    valor %= notas[i]

# Imprime a quantidade de notas de cada tipo
for i in range(7):
    print("{} nota(s) de R$ {},00".format(contador_notas[i], notas[i]))