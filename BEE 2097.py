"""

Dada uma lista de nomes de números, converta-os para inteiros. 
Entrada
Em cada linha (cerca de 100000 linhas), há o nome de um número inteiro n, 0 ≤ n ≤ 1015-1.
Saída
Escreva o número inteiro correspondente ao nome.


Exemplo de Entrada	
zero
cinco
um
nove
dez
quatorze
noventa e nove
cem
cento e um
trezentos e cinquenta e sete
mil
Exemplo de Saída
0
5
1
9
10
14
99
100
101
357
1000
"""












numeros = {
    'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9,
    'dez': 10, 'onze': 11, 'doze': 12, 'treze': 13, 'catorze': 14, 'quinze': 15, 'dezesseis': 16, 'dezessete': 17,
    'dezoito': 18, 'dezenove': 19, 'vinte': 20, 'trinta': 30, 'quarenta': 40, 'cinquenta': 50, 'sessenta': 60,
    'setenta': 70, 'oitenta': 80, 'noventa': 90, 'cem': 100, 'cento': 100, 'duzentos': 200, 'trezentos': 300,
    'quatrocentos': 400, 'quinhentos': 500, 'seiscentos': 600, 'setecentos': 700, 'oitocentos': 800,
    'novecentos': 900, 'mil': 1000, 'milhão': 1000000, 'milhões': 1000000
}

def converte_numero(entrada):
    palavras = entrada.split()
    total = 0
    temp = 0

    for palavra in palavras:
        if palavra == 'e':  # Ignora a conjunção 'e'
            continue
        if palavra in numeros:
            temp += numeros[palavra]
        else:
            total += temp * numeros['milhões' if palavra == 'milhão' else palavra]
            temp = 0

    total += temp
    return total

while True:
    try:
        entrada = input()
        print(converte_numero(entrada))
    except EOFError:
        break
