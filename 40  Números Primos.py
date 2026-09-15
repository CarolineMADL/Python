n1= int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))

if n1 < n2:
    inicio = n1
    fim = n2
else:
    inicio = n2
    fim = n1

print(f"Números primos entre {inicio} e {fim}:")

for num in range(inicio, fim + 1):
    if num > 1:
        d = 0
        
        for i in range(1, num + 1):
            if num % i == 0:
                d = d + 1
        
        if d == 2:
            print(num)