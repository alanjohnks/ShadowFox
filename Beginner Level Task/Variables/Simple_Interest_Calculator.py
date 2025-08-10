print("Store the principal amount, rate of interest, and time in different variables and then "
      "calculate the Simple Interest for 3 years. Formula: Simple Interest = P x R x T / 100")
principal = int(input("Enter the principal amount: "))
rate_of_interest = int(input("Enter the rate of interest: "))
time = int(input("Enter the time(In years): "))
print(f"Your principal amount is {principal}, the rate of interest is {rate_of_interest} and the time is for {time} years.")
simple_interest = (principal*rate_of_interest*time)/100
print(f"Your simple interest is {simple_interest}.")