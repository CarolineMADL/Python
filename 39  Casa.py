cd = int(input("Digite o número da casa: "))

gc = 1

for c in range(1, cd):
    gc=gc*2

print(f"Quantidade de grãos na casa {cd}: {gc}")