x=int(input("Defina o valor de x: "))

y=int(input("Defina o valor de y: "))

if(x>y):
    R = x - y 
    print("O valor de R é: ", R)
elif(x<y):
    R = y - x
    print("O valor de R é: ", R)
else:
    R = 0
    print("O valor de R é: ", R)