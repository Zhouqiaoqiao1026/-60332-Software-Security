# Pointer dereference division by zero
def main():
    a = [0]        # Simulate mutable objects using lists (indirect addressing)
    p = a
    x = 100 // p[0]  # The dereference (value) is 0 -> division by zero
    return x

main()