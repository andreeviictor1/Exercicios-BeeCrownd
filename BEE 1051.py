salario = float(input())

if (salario >= 0) and (salario <= 2000):
    print("Isento")
    
elif (salario > 2000) and (salario <= 3000):
    conta = (salario - 2000.0) * 0.08
    print("R$ %.2f" % conta)
    
elif (salario > 3000) and (salario <= 4500):
    conta = (salario - 3000.0) * 0.18 + (1000.0 * 0.08)
    print("R$ %.2f" % conta)

elif (salario > 4500):
    conta = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print("R$ %.2f" % conta)
