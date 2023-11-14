# Leitura dos dados da peça 1
codigo_peca1, num_peca1, valor_unitario_peca1 = map(float, input().split())

# Leitura dos dados da peça 2
codigo_peca2, num_peca2, valor_unitario_peca2 = map(float, input().split())

# Cálculo do valor total a ser pago
total_a_pagar = (num_peca1 * valor_unitario_peca1) + (num_peca2 * valor_unitario_peca2)

# Impressão do resultado com duas casas decimais
print(f'VALOR A PAGAR: R$ {total_a_pagar:.2f}')
