# Leitura das informações de início
input()
dia_inicio = int(input())
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split())

# Leitura das informações de término
input()
dia_termino = int(input())
hora_termino, minuto_termino, segundo_termino = map(int, input().split())

# Cálculo da duração em segundos
tempo_inicio = dia_inicio * 86400 + hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
tempo_termino = dia_termino * 86400 + hora_termino * 3600 + minuto_termino * 60 + segundo_termino
duracao_segundos = tempo_termino - tempo_inicio

# Cálculo dos dias, horas, minutos e segundos
dias = duracao_segundos // 86400
duracao_segundos %= 86400
horas = duracao_segundos // 3600
duracao_segundos %= 3600
minutos = duracao_segundos // 60
segundos = duracao_segundos % 60

# Saída formatada
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
