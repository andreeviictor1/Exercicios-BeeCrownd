# Leitura dos valores A, B, C e D
A, B, C, D = map(int, input().split())

# Condições para verificar se os valores são aceitos
if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
