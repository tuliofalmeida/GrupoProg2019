# IMC
alturaFloat = 1.59
pesoFloat = 52.0

imc = pesoFloat/(alturaFloat**2)
print(imc)

print("Muito Abaixo do Peso?", imc < 17.0)
print("Abaixo do Peso Normal?", imc >= 17.0 and imc <=18.5)
print("Dentro do Peso Normal?", imc > 18.5 and imc <= 25.0)
print("Acima do Peso Normal?", imc > 25.0 and imc >= 30.0)
print("Muito Acima do Peso?", imc > 30.0)


print("Programa para Calcular IMC")

alturaFloat = input("Digite sua Altura (em metros): ")
pesoFloat = input("Digite seu Peso (em Kg): ")

imc = float(pesoFloat)/(float(alturaFloat)**2)
print(imc)


if imc < 17.0:
    print("Muito Abaixo do Peso")
elif imc >= 17.0 and imc <=18.5:
    print("Abaixo do Peso Normal")
elif imc > 18.5 and imc <= 25.0:
    print("Dentro do Peso Normal")
elif imc > 25.0 and imc >= 30.0:
    print("Acima do Peso Normal")
else:
    print("Muito Acima do Peso")