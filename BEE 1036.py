# Leitura dos valores A, B, C 
A, B, C = map(float, input().split())

#valor de delta 
delta = B**2 - 4*A*C

#verificacao
if A == 0 or delta < 0:
     print("Impossivel calcular")
else:
    x1 = (-B + (delta ** 0.5)) / (2 * A)
    x2 = (-B - (delta ** 0.5)) / (2 * A)
    #impressao com 5 digitos
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
