# Simple BMI Calculator

h = float(input("Enter height in cm: "))
w = float(input("Enter weight in kg: "))

height = (h / 100) ** 2

BMI = (w / height)

BMI = (round (BMI,2))

print("Your BMI is: " , BMI )
