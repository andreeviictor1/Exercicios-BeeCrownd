"""
Nível 1: Se a velocidade é menor que 10 cm/h .
Nível 2: Se a velocidade é maior ou igual a 10 cm/h e menor que 20 cm/h .
Nível 3: Se a velocidade é maior ou igual a 20 cm/h .

A primeira linha contém um inteiro L (1 ≤ L ≤ 500) representando o número de lesmas do grupo

egunda linha contém L inteiros Vi (1 ≤ Vi ≤ 50) representando as velocidades de cada lesma do grupo.
Exemplo de Entrada

10
10 10 10 10 15 18 20 15 11 10
10
1 5 2 9 5 5 8 4 4 3
10
19 9 1 4 5 8 6 11 9 7

Exemplo de Saída
3
1
2
"""




def nivel_velocidade(velocidades):
    nivel_1 = 0 
    nivel_2 = 0
    nivel_3 = 0
    
    for velocidade in velocidades:
        if velocidade < 10 :
            nivel_1 += 1 
        elif velocidade < 20 :
            nivel_2 += 1 
        else:
            nivel_3 += 1
    
    if nivel_3 > 0:
        return 3 
    elif nivel_2 > 0:
        return 2
    else:
        return 1
    
    
# LER O NUMERO DE GRUPOS 
num_grupos = int(input())

for _ in range(num_grupos):
    #ler velocidade de cada um no grupo 
    velocidades = list(map(int, input().split()))
    
    
    resultado = nivel_velocidade(velocidades)
    print(resultado)