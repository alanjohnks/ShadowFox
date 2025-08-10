# 3. Write a program to check if two cities belong to the same country.
# Ask the user to enter two cities and print whether they belong to the
# same country or not.
print("Program to check if two cities belong to the same country.")
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
print("Please start the city name with capital letter!..")
user_input1 = input("Enter name of the first city: ")
user_input2 = input("Enter name of the second city: ")
if user_input1 in Australia and user_input2 in Australia:
    print(f"Both cities are in Australia.")
elif user_input1 in UAE and user_input2 in UAE:
    print(f"Both cities are in UAE.")
elif user_input1 in India and user_input2 in India:
    print(f"Both cities are in India.")
else:
    print("They don't belong to the same country.")