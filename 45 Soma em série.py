s = 0

for n in range(1, 16):
    d = n * n
    
    if n % 2 == 0:
        s = s - (n / d)
    else:
        s = s + (n / d)

print(f"Resultado da série: {s}")