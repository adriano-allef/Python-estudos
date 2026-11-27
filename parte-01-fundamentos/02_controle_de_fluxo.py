idade = int(input("Qual sua idade?"))

if (idade < 18):
    print(f"Menor de Idade!")

elif (idade >= 18 and idade <= 59):
    print(f"Adulto")

else: 
    print(f"Idoso")