X = int(input())
contagem = 0  # Variável para controlar a contagem de números ímpares

while contagem < 6:
    if X % 2 != 0:
        print(X)
        contagem += 1
    X += 1
