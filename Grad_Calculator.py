# Grade Calculator
percentage = float(input("Enter your percentage score: "))

if percentage >= 90:
    grade = "A+"
elif 80 <= percentage < 90:
    grade = "A"
elif 70 <= percentage < 80:
    grade = "B"
elif 60 <= percentage < 70:
    grade = "C"
elif 50 <= percentage < 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is", grade)