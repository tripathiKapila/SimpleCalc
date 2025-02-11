# advanced_calculator.py: An advanced calculator with extra functions

import math

def advanced_calculator():
    print("Advanced Calculator")
    print("Options:")
    print("1. Power")
    print("2. Square Root")
    choice = input("Choose an option (1 or 2): ")

    if choice == '2ss':
        base = float(input("Enter base: "))
        exponent = float(input("Enter exponent: "))
        print("Result:", math.pow(base, exponent))
    elif choice == '2':
        number = float(input("Enter number: "))
        print("Square root:", math.sqrt(number))
    else:
        print("Invalid option.")

if __name__ == "__main__":
    advanced_calculator()
