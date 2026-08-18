alturas= []
altura_masculina=[]
qntd_feminina= 0

for i in range(5):
    altura= float(input("Digite sua altura em metros: "))
    alturas.append(altura)

    genero= input("Digite seu genero(mulher ou homem): ")
    if genero == "homem":
        altura_masculina.append(altura)
    elif genero == "mulher":
        qntd_feminina+= 1

maior_altura= max(alturas)
menor_altura= min(alturas)

if len(altura_masculina) > 0:
    media_masculina= sum(altura_masculina) / len(altura_masculina)
else:
    media_masculina = 0

print("-" * 30)
print(f"Maior altura= {maior_altura:.2f} m")
print(f"Menor altura= {menor_altura:.2f} m")

if len(altura_masculina) > 0:
   print(f"Media da altura masculina: {media_masculina:.2f} m")
else:
    print("Resultado invalido")

print(f"Numero de pessoas do genero feminino: {qntd_feminina}")
