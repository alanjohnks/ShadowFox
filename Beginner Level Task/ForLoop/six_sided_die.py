# 1. Using a for loop, simulate rolling a six-sided die multiple times (at least 20 times).
# Count and print the following statistics:
# How many times you rolled a 6
# How many times you rolled a 1
# How many times you rolled two 6s in a row

import random
sixes = 0
ones = 0
double_sixes = 0
value_list = []
for i in range(20):
    die_value = random.randint(1,6)
    value_list.append(die_value)
    if die_value == 6:
        sixes+=1
    elif die_value == 1:
        ones += 1
    if value_list[i-1] == 6 and die_value == 6:
        double_sixes += 1
print(value_list)
print(sixes)
print(ones)
print(double_sixes)