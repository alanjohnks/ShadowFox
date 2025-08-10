print("In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond \n"
      "using the formula: Circle Area = πr^2. (Use the value 3.14 for π) \n"
      "Bonus Question: If there is exactly 1.4 liters of water in a square meter, \n"
      "what is the total amount of water in the pond? Print the answer without any decimal point in it. \n"
      "Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter")
radius = 84
pi = 22/7
area = pi*radius*radius
water_in_pond = round(1.4*area)
print(f"The area of the pond is {round(area)} square metre.")
print(f"The total amount of water in the pond is {water_in_pond} litres.")