#Vm=valor mensal Pr_a=Preço atual Pr_n=Preço novo
Vm= float(input("Digite o valor mensal: "))
Pr_a= float(input("Digite o preço atual: "))
if(Vm<500 and Pr_a<30):
    Pr_n= Pr_a*1.10
elif (Vm>=500 and Vm<1000 and Pr_a<=30 and Pr_a<80):
    Pr_n= Pr_a*1.15
elif (Vm>=1000 and Pr_a>=80):
    Pr_n= Pr_a*0.95
else:
    Pr_n=Pr_a
print("O preço novo é: ", Pr_n)

    