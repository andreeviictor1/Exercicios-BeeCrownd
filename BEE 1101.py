while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    menor, maior = min(m, n), max(m, n)
    soma = sum(range(menor, maior + 1))
    sequencia = ' '.join(map(str, range(menor, maior + 1)))
    print(f'{sequencia} Sum={soma}')
