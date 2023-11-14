consumo = 12
tempo_viagem = int(input())
velocidade_media = int(input())
distancia_percorrida = tempo_viagem * velocidade_media
litros_necessarios = distancia_percorrida / consumo
print("{:.3f}".format(litros_necessarios))