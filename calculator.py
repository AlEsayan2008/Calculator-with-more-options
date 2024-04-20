import math
while True:
    first_number = int(input("Enter first number`"))
    operator = input("Enter any operator`")
    second_number = int(input("Enter second number`"))


    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        print(first_number / second_number)
    elif operator == "//":
        print(first_number // second_number)
    elif operator == "%":
        print(first_number % second_number)
    elif operator == "**":
        print(first_number ** second_number)
    elif operator == "abs":
        print(abs(first_number, second_number))
    elif operator == "max":
        print(max(first_number, second_number))
    elif operator == "min"
        print(min(first_number, second_number))
    elif operator == "(a+b)**2":
        print((first_number ** 2 + 2 * first_number * second_number + second_number ** 2))
    elif operator == "(a-b)**2":
        print(first_number ** 2 - 2 * first_number * second_number + second_number ** 2)
    elif operator == "a**2-b**2":
        print((first_number + second_number) * (first_number - second_number))
    elif operator == "a**3+b**3":
        print((first_number + second_number) * (first_number ** 2 - first_number * second_number + second_number ** 2))
    elif operator == "a**3-b**3":
        print((first_number - second_number) * (first_number ** 2 + first_number * second_number + second_number ** 2))
    elif operator == "(a+b)**3":
        print(first_number ** 3 + 3 * first_number ** 2 * second_number + 3 * first_number * second_number ** 2 + second_number ** 3)
    elif operator == "(a-b)**3":
        print(first_number ** 3 - 3 * first_number ** 2 * second_number + 3 * first_number * second_number ** 2 - second_number ** 3)
    elif operator == "sqrt.a":
        print(math.sqrt(first_number))
    elif operator == "sqrt.b":
        print(math.sqrt(second_number))
    elif operator == "factorial.a":
        print(math.factorial(first_number))
    elif operator == "factorial.b":
        print(math.factorial(second_number))
    elif operator == "sin.a":
        print(math.sin(first_number))
    elif operator == "sin.b":
        print(math.sin(second_number))
    elif operator == "cos.a":
        print(math.cos(first_number))
    elif operator == "cos.b":
        print(math.cos(second_number))
    elif operator == "tan.a":
        print(math.tan(first_number))
    elif operator == "tan.b":
        print(math.tan(second_number))
    elif operator == "cbrt.a":
        print(math.cbrt(first_number))
    elif operator == "cbrt.b":
        print(math.cbrt(second_number))
    else:
        print("You write wrong operator:") 
