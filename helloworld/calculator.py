def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


request = int(input("\n Enter 1 to add and 2 to subtract.  "))
num1 = int(input("\n Enter the first number.  "))
num2 = int(input("\n Enter the second number.  "))

if request == 1:
    print("\n", num1, "+", num2, "=", add(num1, num2))
elif request == 2:
    print("\n", num1, "-", num2, "=", subtract(num1, num2))
else:
    print("\n Invalid option.")


