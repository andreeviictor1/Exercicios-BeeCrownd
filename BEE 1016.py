# Lê a distância em quilômetros
distancia = int(input())

# Velocidades dos carros
velocidade_x = 60  # em Km/h
velocidade_y = 90  # em Km/h

# Calcula o tempo necessário em horas para o carro Y alcançar o carro X
tempo_em_horas = distancia / (velocidade_y - velocidade_x)

# Converte o tempo de horas para minutos
tempo_em_minutos = tempo_em_horas * 60

# Imprime o resultado
print(f'{int(tempo_em_minutos)} minutos')
