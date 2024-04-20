#Who doesn't understand I'm explain my code:
#At first I create an infinity loop in order to use calculator infinity times.
#Then I give inputs for user.
#After That I use if else and elif statement in order to check operator sign.
#After checking I performed the action according to the corresporanding token

infinity_loop_condition = "Continue"
while infinity_loop_condition == "Continue":
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
    elif operator == "(a+b)**2":
        print((first_number**2+2*first_number*second_number + second_number**2))
    else:
        print("You write wrong operator:")
#This project not finished 
