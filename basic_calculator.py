# basic_calculator.py: A simple interactive calculator

def calculator():
    print("Basic Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    # Handle division carefully
    print("Division:", a / b if b != 0 else "Error: Division by zero")

if __name__ == "__main__":
    calculator()
