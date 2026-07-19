import math

while True:
    operation = input("Choose an operation (+, -, *, /, sin, cos) or type 'end' to exit: ")

    if operation.lower() == "end":
        print("Calculator shutting down...")
        break

    # addition 
    if operation == "+":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)

    # minus
    elif operation == "-":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)

    # Multiplication
    elif operation == "*":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 * num2)

    # Division
    elif operation == "/":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", num1 / num2)

    # Sin
    elif operation == "sin":
        angle = float(input("Enter angle: "))
        unit = input("Is the angle in Degrees or Radians? (d/r): ").lower()

        if unit == "d":
            angle = math.radians(angle)

        print("Result:", math.sin(angle))

    # Cosin
    elif operation == "cos":
        angle = float(input("Enter angle: "))
        unit = input("Is the angle in Degrees or Radians? (d/r): ").lower()

        if unit == "d":
            angle = math.radians(angle)

        print("Result:", math.cos(angle))

    # Invalid 
    else:
        print("Invalid operation. Please try again.")

    print()
