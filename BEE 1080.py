# Inicialize as variáveis para armazenar o maior valor e sua posição
maior_valor = -1  # Inicializado com um valor mínimo para garantir que qualquer valor seja maior
posicao = -1

# Loop para ler os 100 valores
for i in range(1, 11):
    valor = int(input())

    # Verifica se o valor atual é maior que o maior valor encontrado até agora
    if valor > maior_valor:
        maior_valor = valor
        posicao = i

# Imprime o maior valor e sua posição
print(maior_valor)
print(posicao)
