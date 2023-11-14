"""
Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

Exemplo de Entrada
5

Exemplo de Saída
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125

"""

N = int(input())

for i in range (1, N + 1):
    primeiro_numero = i 
    segundo_numero = i ** 2
    terceiro_numero = i ** 3
    
    print(f'{primeiro_numero} {segundo_numero} {terceiro_numero}') 