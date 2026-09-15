#nv= número de voltas em=extensão do circurto em metros
#dt_km=distância em km t_h=tempo em horas t_m=tempo em minutos
#vm=velocidade média em km/h

nv= int(input("Digite o número de voltas: "))
em= float(input("Digite a extensão do circuito em metros: "))
t_m= float(input("Digite o tempo em minutos: "))

dt_km= (nv*em)/1000
t_h= t_m/60
vm= dt_km/t_h
print("A velocidade média é de: ", vm, "km/h")
