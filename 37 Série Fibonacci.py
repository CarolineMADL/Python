n=int(input("Digite um número : "))
t1=1
t2=1
print("Série de Fibonacci:")
for i in range (n):
    print(t1)
    t1,t2 = t2,t1 + t2
    
    