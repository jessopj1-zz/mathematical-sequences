import os
mylist = []
order = 1
value = 1
print("This is John's square number generator.")
print("The first is ", value)
iterations = input("How many square numbers would you like to generate? I suggest at least 10: ")
print("You chose to get the fisrt ", iterations, " square numbers" )

while (order < int(iterations)):
    mylist.append(int(order))
    order = int(order) + 1
    value = sum(mylist)
    print("Value = ", value)

print("That is the first ",iterations ," square numbers")
os.system("pause")
