n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
if (n1>n2):
    maior=n1
    menor=n2
else:
    maior=n2
    menor=n1
if(menor==0):
    print("Não é possível verificar ")
elif(maior%menor==0):
    print(f"{maior} é multiplo de {menor}")
else:
    print(f"{maior} não é multiplo de {menor}")
    
