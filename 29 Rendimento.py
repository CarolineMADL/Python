#vi=valor do investimento vc=valor corrigido
print("Escolha o tipo de investimento: ")
print("[1] Poupança")
print("[2] Renda Fixa") 
esc = int(input("Digite a opção desejada: "))
vi= float(input("Digite o valor do investimento: "))
if(esc==1):
    vc= vi * 1.03
    print("O valor corrigido é: ", vc)
elif(esc==2):
    vc= vi * 1.05
    print("O valor corrigido é: ", vc)
else:
    print("Opção inválida!")

