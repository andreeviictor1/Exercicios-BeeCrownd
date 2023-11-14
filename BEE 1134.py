# Inicialize contadores para cada tipo de combustível
alcool = gasolina = diesel = 0

while True:
    # Leia o código do combustível
    codigo = int(input())
    
    if codigo == 4:
        # Se o código for 4, encerre o loop
        break
    elif 1 <= codigo <= 3:
        # Caso seja um código válido, incrementar o contador apropriado
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1
    else:
        # Se for um código inválido, peça ao usuário para inserir um novo código
        continue

# Imprima a mensagem de agradecimento e as quantidades
print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)
