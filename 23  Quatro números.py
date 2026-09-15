N1=int(input("Adicione um número em ordem crescente: "))
N2=int(input("Adicione outro número em ordem crescente: "))
N3=int(input("Adicione mais um número em ordem crescente: "))
N4=int(input("Adicione o último número qualquer: "))

if(N4>N3):
    print(N1,N2,N3,N4)
elif(N4>N2):
        print(N1,N2,N4,N3)
elif(N4>N1):
        print(N1,N4,N2,N3)
else:
      print(N4,N1,N2,N3)  