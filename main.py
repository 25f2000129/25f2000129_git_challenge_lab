#main python file for all feature execution

from sum import *
from divide import *
from multiply import *
from subtraction import *

print("Options::\n1 --> sum\n2 --> subtraction\n3 --> multiply\n4 --> divide\n0 --> exit")

while 1:
    choice = int(input("Enter Option:"))

    if choice in range(1,5): 
        a = int(input("Enter num1:"))
        b = int(input("Enter num2:"))
        if choice == 1:
            print(sum(a,b))
        elif choice == 2:
            print(subtract(a,b))
        elif choice == 3:
            print(multiply(a,b))
        elif choice == 4:
            print(divide(a,b))
    elif choice == 0:
            print("Exiting...")
            break
    else:
        print("invalid choice")