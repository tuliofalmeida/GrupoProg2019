print("IMC Calculator 3000")

altura = input("Digita sua altura - em metros -:")
peso = input("Digite seu peso - em kilos -:")
IMC = float(peso)/(float(altura)**2)
print("Seu IMC ="+str(IMC))

if IMC<17.0:
    print("Voce esta desnutrido!")
elif IMC>17.0 and IMC<=18.5:
    print("Voce esta abaixo do peso!")
elif IMC>18.5 and IMC<=25.0:
    print("Seu peso esta dentro do normal!", )
elif IMC>25.0 and IMC<=30.0:
    print("Voce esta acima do peso!")
else:
    print("Voce esta gordo!")


