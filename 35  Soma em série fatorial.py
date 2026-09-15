n=int(input("Adicione o número :"))
soma=1.0
for i in range(1,n+1):
    fat=1
    for j in range(1,i+1):
        fat=fat*j
    soma=soma+(1/fat)
print("O valor da soma de séries é : ",soma)
