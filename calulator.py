num1 = float(input("enter first number"))
num2 = float(input("enter second number"))

print("press 1 for addition\n press 2 for subtraction\n press 3 for multiplication\n press 4 for division")


choice = int(input("your choice 1 to 4"))

if choice == 1:
    print("add",num1 + num2)
elif choice == 2:
    print("sub",num1 - num2)
elif choice == 3:
    print("multiply",num1 * num2)
elif choice == 4:
    print('divide',num1/num2)
else:
    print('syntax error')
