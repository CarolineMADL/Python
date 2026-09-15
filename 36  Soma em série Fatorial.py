n=int(input("Adicione um número: "))
soma=1
for i in range(1,n+1,1):
    fat=1
    for j in range (1,i+1,1):
        fat= fat*j
soma= soma + (1/fat)
print(f" A soma de series fatorial é {soma}")
