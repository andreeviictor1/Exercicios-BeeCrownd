# Leia a hora de início e a hora de fim do jogo
hora_inicio, hora_fim = map(int, input().split())

# Calcula a duração do jogo
if hora_inicio < hora_fim:
    duracao = hora_fim - hora_inicio
else:
    duracao = 24 - hora_inicio + hora_fim

# Aplica as restrições de 1 a 24 horas
if duracao < 1:
    duracao = 24 + duracao
elif duracao > 24:
    duracao = duracao % 24

# Apresenta a duração do jogo
print(f"O JOGO DUROU {duracao} HORA(S)")