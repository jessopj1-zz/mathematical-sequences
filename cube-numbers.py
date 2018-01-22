import os
order = 1
print("This is John's cube number generator.")
print("The first is ", value)
value = int(value) + int(value2)
iterations = input("How many cube numbers would you like to generate? I suggest at least 10: ")
print("You chose to get the fisrt ", iterations, " cube numbers" )

while (order < int(iterations)):
    order = int(order) + 1
    value = order**3
    print("Value = ", value)

print("That is the first ",iterations ," cube numbers")
os.system("pause")
