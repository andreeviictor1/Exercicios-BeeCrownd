valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    quantidade_nota = int(valor / nota)
    print("{} nota(s) de R$ {:.2f}".format(quantidade_nota, nota))
    valor -= quantidade_nota * nota

print("MOEDAS:")
for moeda in moedas:
    quantidade_moeda = int(round(valor, 2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantidade_moeda, moeda))
    valor -= quantidade_moeda * moeda
