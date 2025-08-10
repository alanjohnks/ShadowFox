# Write a program to determine the BMI Category based on user input.
print("BMI Calculator")

# Ask the user to:
# Enter height in meters
# Enter weight in kilograms
height = int(input("Enter your height (in cm): "))
weight = int(input("Enter your weight (in kg): "))
height_in_metres = height/100

# Calculate BMI using the formula: BMI = weight / (height)2
BMI = round(weight/(height_in_metres**2),1)

# Use the following categories:
# If BMI is 30 or greater, print "Obesity"
if BMI >= 30:
    print(f"Your BMI is {BMI}. You are Obese")
# If BMI is between 25 and 29, print "Overweight"
elif BMI >= 25:
    print(f"Your BMI is {BMI}. You are Overweight")
# If BMI is between 18.5 and 25, print "Normal"
elif BMI >= 18.5:
    print(f"Your BMI is {BMI}. You are Normal")
# If BMI is less than 18.5, print "Underweight"
elif BMI > 0:
    print(f"Your BMI is {BMI}. You are Underweight")
else:
    print("The details might are invalid please check again.")