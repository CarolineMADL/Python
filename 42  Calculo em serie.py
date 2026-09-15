#s=soma d=denominador n=numerador
s = 0
d = 1

for n in range(1, 51):
    s = s + (n / d)
    d = d + 2

print(f"Resultado da série: {s}")