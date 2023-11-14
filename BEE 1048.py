salario = float(input())

if salario > 0 and salario <= 400:
    reajuste = 0.15
    novo_salario = (salario * reajuste) + salario
    reajuste_ganho = novo_salario - salario
    percentual = reajuste * 100 
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print(f'Em percentual: {percentual:.0f} %')

elif salario > 400 and salario <= 800:
    reajuste = 0.12
    novo_salario = (salario * reajuste) + salario
    reajuste_ganho = novo_salario - salario
    percentual = reajuste * 100 
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print(f'Em percentual: {percentual:.0f} %')

elif salario > 800 and salario <= 1200:
    reajuste = 0.10
    novo_salario = (salario * reajuste) + salario
    reajuste_ganho = novo_salario - salario
    percentual = reajuste * 100 
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print(f'Em percentual: {percentual:.0f} %')

elif salario > 1200 and salario <= 2000:
    reajuste = 0.07
    novo_salario = (salario * reajuste) + salario
    reajuste_ganho = novo_salario - salario
    percentual = reajuste * 100
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print(f'Em percentual: {percentual:.0f} %')

elif salario > 2000:
    reajuste = 0.04
    novo_salario = (salario * reajuste) + salario
    reajuste_ganho = novo_salario - salario
    percentual = reajuste * 100
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste_ganho:.2f}')
    print(f'Em percentual: {percentual:.0f} %')