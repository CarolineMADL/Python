#Raizes Reais
A=int(input("Digite o valor de A: "))
B=int(input("Digite o valor de B: "))
C=int(input("Digite o valor de C: ")) 
delta = (B**2) - (4*A*C)
if delta < 0:
    print("Não existem raízes reais")
elif delta == 0:    
    raiz = -B / (2*A)
    print("Existe apenas uma raiz real:", raiz)
else:
    raiz1 = (-B + delta**0.5) / (2*A)
    raiz2 = (-B - delta**0.5) / (2*A)
    print("As raízes reais são:", raiz1, "e", raiz2)    
    