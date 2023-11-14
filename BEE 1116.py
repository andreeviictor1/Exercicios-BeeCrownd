n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        resultado = x / y
        print(f'{resultado:.1f}')
