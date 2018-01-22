import os
order = 1
print("This is John's square number generator.")
print("The first is ", value)
value = int(value) + int(value2)
iterations = input("How many square numbers would you like to generate? I suggest at least 10: ")
print("You chose to get the fisrt ", iterations, " square numbers" )

while (order < int(iterations)):
    order = int(order) + 1
    value = order**2
    print("Value = ", value)

print("That is the first ",iterations ," square numbers")
os.system("pause")
