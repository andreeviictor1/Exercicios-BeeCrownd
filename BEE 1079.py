casos = int(input())


for i in range (casos):
    x1, x2, x3 = map(float, input().split())
    media = (x1 * 2 + x2 * 3 + x3 * 5) / (2 + 3 + 5)
    print(f'{media:.1f}')