# Division of function parameters by zero
def divide(a: int, b: int) -> int:
    return a // b

def main():
    result: int = divide(10, 0)  # should raise ZeroDivisionError
    return result

main()