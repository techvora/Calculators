# BMI Calculator(BODY MASS INDEX)
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You are normal weight")
elif 25 <= bmi < 30:
    print("You are overweight")
else:
    print("You are obese")
