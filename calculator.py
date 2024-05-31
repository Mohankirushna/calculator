"""calculator"""

while True:
    num1 = int(input('enter the first number:'))
    num2 = int(input("enter the second number:"))
    print("""
              1.add
              2.sub
              3.mul
              4.div""")
    operator = int(input('enter the operation you want to perform'))
    if operator == 1:
        print("the sum of numbers=", num1 + num2)
    elif operator == 2:
        if num1 < num2:
            print("the difference=", num2 - num1)
        elif num1 > num2:
            print("the difference=", num1 - num2)
    elif operator == 3:
        print("the answer is=", num1 * num2)
    elif operator == 4:
        if num2 != 0:
            print("the answer is=", num1 / num2)
        else:
            print("Cannot divide by zero.")
    else:
        print("enter the correct number to calculate")

    choice = input("Do you want to continue? (Enter '1' to continue, any other key to exit): ")

    if choice != '1':
        print("Exiting...")
        break
    else:
        print("Continuing...")
