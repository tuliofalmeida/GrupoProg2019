varPeso = 72.0
varAltura = 1.84

IMC = varPeso/(varAltura**2)

print(IMC)

print("IMC muito abaixo do peso:", IMC<17.0)
print("IMC abaixo do peso:", IMC>17.0 and IMC<=18.5)
print("IMC peso dentro do normal:", IMC>18.5 and IMC<=25.0)
print("IMC acima do normal:", IMC>25.0 and IMC<=30.0)
print("IMC muito acima do normal:", IMC>30.0)