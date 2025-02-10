from calculator import add, subtract, multiply, divide
from utils import format_result

def main():
    a, b = 10, 5

    result_add = add(a, b)
    result_subtract = subtract(a, b)
    result_multiply = multiply(a, b)
    result_divide = divide(a, b)
    print("Result of addition (from branch B):", format_result(add(a, b)))

    print(format_result(result_add))
    print(format_result(result_subtract))
    print(format_result(result_multiply))
    print(format_result(result_divide))

if __name__ == "__main__":
    main()
