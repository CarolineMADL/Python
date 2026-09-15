N1=float(input("Adicione a primeira nota: "))

N2=float(input("Adicione a segunda nota: "))

N3=float(input("Adicione a terceira nota: "))

N4=float(input("Adicione a quarta nota: "))

Média=(N1+N2+N3+N4)/4

if (Média>=6):
    print("Aprovado com média:", Média)
elif (Média>=3 and Média< 6):
    print("Exame com média:", Média)
else:
    print("Retido com média:", Média)
    
