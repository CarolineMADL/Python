#Salário
# Horas trabalhadas = HT # Valor por hora = VH
#Percentual de desconto = PD Numero de dependentes = ND
HT = int(input("Digite o número de horas trabalhadas: "))
VH = float(input("Digite o valor por hora: "))
PD = float(input("Digite o percentual de desconto: "))
ND = int(input("Digite o número de dependentes: "))
SalarioBruto = HT * VH
Desconto = SalarioBruto * (PD / 100)
SalarioLiquido = SalarioBruto - Desconto + (ND * 100)
print("Salário LIquido: R$", SalarioLiquido)
