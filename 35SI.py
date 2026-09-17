n1=int(input("Adicione um número: "))
n2=int(input("Adicione um segundo número: "))
if(n1>n2):
    nm=n2
    nma=n1
else:
    nm=n1
    nma=n2
soma=0
for nm in range (nm,nma+1):
    if (nm%2 !=0):
        soma=soma+nm
print(f"A soma dos impares entre os numeros {n1} e {n2} é {soma}")

