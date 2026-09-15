nu = -1.0
while nu <= 0:
    nu = float(input("Digite o 1º número positivo: "))

vma = nu
vm = nu

for i in range(2, 101):
    nu = -1.0
    while nu <= 0:
        nu = float(input(f"Digite o {i}º número positivo: "))
    
    if nu > vma:
        vma = nu
        
    if nu < vm:
        vm = nu

print(f"\nO maior valor digitado (vma) foi: {vma}")
print(f"O menor valor digitado (vm) foi: {vm}")
