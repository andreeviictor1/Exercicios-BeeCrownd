"""
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] 
e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), 
que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
 

Saída
Para cada caso, imprima quantos números estão dentro (in) 
e quantos valores estão fora (out) do intervalo.
"""




def count(condicao):
    count_in = 0 
    count_out = 0
    
    for numeros in condicao:
        if 10 <= numeros <= 20:
            count_in += 1
        else:
            count_out += 1
            
    return count_in, count_out
num_casos = int(input())


for _ in range(num_casos):
    numeros = list(map(int, input().split()))
    dentro, fora = count(numeros)
    print(f'{dentro} in 
          {fora} out')



