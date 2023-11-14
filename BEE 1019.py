# Lê o valor inteiro em segundos
tempo_em_segundos = int(input())

# Calcula as horas, minutos e segundos
horas = tempo_em_segundos // 3600
tempo_em_segundos %= 3600
minutos = tempo_em_segundos // 60
segundos = tempo_em_segundos % 60

# Imprime o tempo formatado
print(f'{horas}:{minutos}:{segundos}')
