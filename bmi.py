heightFloat = 1.74
WeightFloat = 64.0
BMI = WeightFloat/(heightFloat**2)

print(BMI)

print("Too underweight?", BMI < 17.0)
print("Underweight?", BMI >= 17.0 and BMI <= 18.5)
print("Weight within normal?", BMI > 18.5 and BMI <= 25.0)
print("Overweight?", BMI > 25.0 and BMI <= 30.0)
print("Too overweight?", BMI > 30.0)