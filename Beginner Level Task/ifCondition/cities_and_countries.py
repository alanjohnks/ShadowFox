# 2. Write a program to determine which country a city belongs to. Given
# list of cities per country:
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
# Ask the user to enter a city name and print the corresponding country.
user_input = input("Enter a city name(Please start the city name with capital letter): ")
if user_input in Australia:
    print(f"{user_input} is in Australia.")
elif user_input in UAE:
    print(f"{user_input} is in UAE.")
elif user_input in India:
    print(f"{user_input} is in India.")
else:
    print(f"The given input is incorrect or not in the lists present. \n"
          f"This is the input given: {user_input}.\n")