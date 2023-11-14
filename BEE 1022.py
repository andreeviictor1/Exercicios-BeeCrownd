from fractions import Fraction

# Função para realizar a operação matemática
def calcular(expressao):
    # Separar a expressão nos operadores e operandos
    n1, operador, n2 = expressao.split()
    num1, den1 = map(int, n1.split('/'))
    num2, den2 = map(int, n2.split('/'))
    
    # Realizar a operação de acordo com o operador
    if operador == '+':
        resultado = Fraction(num1, den1) + Fraction(num2, den2)
    elif operador == '-':
        resultado = Fraction(num1, den1) - Fraction(num2, den2)
    elif operador == '*':
        resultado = Fraction(num1, den1) * Fraction(num2, den2)
    elif operador == '/':
        resultado = Fraction(num1, den1) / Fraction(num2, den2)
    
    return resultado

# Função para simplificar a fração, se possível
def simplificar_fracao(resultado):
    return f"{resultado} = {resultado.numerator}/{resultado.denominator}"

# Número de casos de teste
num_casos = int(input("Digite a quantidade de casos de teste: "))

# Loop para lidar com cada caso de teste
for _ in range(num_casos):
    expressao = input("Digite a expressão (no formato 'a/b + c/d'): ")
    resultado = calcular(expressao)
    resultado_simplificado = simplificar_fracao(resultado)
    print(resultado_simplificado)
