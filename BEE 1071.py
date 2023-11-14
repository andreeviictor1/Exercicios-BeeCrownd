X = int(input())
Y = int(input())

soma_impares = 0 

if X > Y :
    X, Y = Y, X 
    
    
for i in range (X + 1, Y):
    if i % 2 != 0: 
        soma_impares += 1 
        
print(soma_impares)