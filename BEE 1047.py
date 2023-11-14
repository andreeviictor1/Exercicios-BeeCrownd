hora_inicial, minuto_inicial, hora_final, minuto_final  = map(int,input().split())

#Duracao 



if (hora_final > hora_inicial) and (minuto_final > minuto_inicial):
    duracao_horas = hora_final - hora_inicial
    duracao_minutos = minuto_final - minuto_inicial
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')
    
elif (hora_final > hora_inicial) and (minuto_inicial > minuto_final):
    duracao_horas = (hora_final - hora_inicial) - 1 
    duracao_minutos = (minuto_final - minuto_inicial) + 60
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')
    
elif (hora_final == hora_inicial) and (minuto_inicial > minuto_final):
    duracao_horas = 23
    duracao_minutos = (minuto_final - minuto_inicial) + 60
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')
    
elif (hora_final == hora_inicial) and (minuto_final > minuto_inicial):
    duracao_horas = 0
    duracao_minutos = minuto_final - minuto_inicial
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')
 
elif (hora_final > hora_inicial) and (minuto_final == minuto_inicial):
    duracao_horas = hora_final - hora_inicial
    duracao_minutos = 0
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')

elif (hora_final < hora_inicial) and (minuto_final == minuto_inicial):
    duracao_horas = (hora_final - hora_inicial) + 24
    duracao_minutos = 0 
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')
    
elif (hora_inicial > hora_final) and (minuto_final > minuto_inicial):
    duracao_horas = (hora_final - hora_inicial) + 23
    duracao_minutos = (minuto_final - minuto_inicial) + 60
    print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)')
else:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    
    
