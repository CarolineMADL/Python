#hi=hora inicio mi=minutos inicio hf=hora final mf=minutos final 
#dur_h= duração em horas dur_m= duração em minutos

hi=int(input("Digite a hora de início: "))
mi=int(input("Digite os minutos de início: "))
hf=int(input("Digite a hora de término: "))
mf=int(input("Digite os minutos de término: "))

if(hf<hi):
    hf=hf+24
else:
    hf=hf
if(mf<mi):
    mf=mf+60
    hf=hf-1
dur_h=hf-hi
dur_m=mf-mi
print("O jogo durou %d hora(s) e %d minuto(s)"%(dur_h,dur_m))
