# 2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.
# Write a program that:
# Asks you to perform 10 jumping jacks at a time.
# After each set, it asks, "Are you tired?"
print("Complete 100 jumping jacks.")
finished = False
total = 100
count = 0
while (not finished and count != 100):
    print("Perform 10 Jumping Jacks!..")
    count += 10
    total -= 10
    user_condition = input("Are you tired?(yes/no): ")
    if user_condition == 'yes' or user_condition == 'y':
        skip_or_not = input("Do you want to skip the remaining sets?(yes/no): ")
        if skip_or_not == 'yes' or skip_or_not == 'y':
            print(f"You completed a total of {count} jumping jacks.")
            finished = True
        else:
            print(f"{total} jumping jacks are remaining.")
if count == 100:
    print("Congratulations! You completed the workout.")
    finished=True

