import math

def calculator_func():    
    while True:
        cmd = input("\nDo you want to use calculator?\n")
        if cmd.lower() == "yes":
            problem = input("\nWrite any problem for solving\n")
            result = eval(problem)
            print(f"\nResult: {result}")
        elif cmd.lower() == "no":
            print("Exiting calculator")
            break
        else:
            print("Wrong command: Please try again")
        

calculator_func()
