# Leitura das quatro notas
N1, N2, N3, N4 = map(float, input().split())

# Calculo da média ponderada
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4) / 10

# Imprimir a média com uma casa decimal
print("Media: {:.1f}".format(media))

# Verificar se o aluno está aprovado, reprovado ou em exame
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: {:.1f}".format(nota_exame))
    media_final = (media + nota_exame) / 2
    print("Aluno aprovado." if media_final >= 5.0 else "Aluno reprovado.")
    print("Media final: {:.1f}".format(media_final))
