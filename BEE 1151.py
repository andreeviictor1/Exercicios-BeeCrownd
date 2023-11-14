def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Lê o valor de N
N = int(input())

# Verifica se N está dentro do intervalo permitido
if 0 < N < 46:
    # Gera a sequência de Fibonacci com os N primeiros números
    result = fibonacci(N)
    
    # Mostra os valores na mesma linha, separados por um espaço
    print(*result, sep=" ")
