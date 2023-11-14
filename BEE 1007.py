# Read four integer values named A, B, C and D. Calculate and print the difference of product A and B by the product of C and D (A * B - C * D).

# Input
# The input file contains 4 integer values.

# Output
# Print DIFERENCA (DIFFERENCE in Portuguese) with all the capital letters, according to the following example, with a blank space before and after the equal signal.

# DEFININDO VARIAIS A, B, C, D 
A,B,C = map(float, input().split())

# Cálculo das áreas
area_triangulo = 0.5 * A * C
area_circulo = 3.14159 * C ** 2
area_trapezio = 0.5 * (A + B) * C
area_quadrado = B ** 2
area_retangulo = A * B

# Impressão das áreas com 3 dígitos após o ponto decimal
print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
