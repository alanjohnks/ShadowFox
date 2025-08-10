print("Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return \n"
      "a formatted string. Print the result. Try to identify the representation used.")
def format(num,alphabet):
    number = num
    string = alphabet
    return f"The number is {number}, the alphabet is {string}."
result = format(145,'o')
print(result)