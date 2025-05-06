# Division by zero in conditional statements
def main():
    a = 1
    b = 0
    if a > 0:
        c = a // b  # Only one path leads to division by zero
    return 0

main()