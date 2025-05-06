# Divide the array index by zero
def main():
    a = [1, 0, 2]
    i = 1
    x = 10 // a[i]  # a[1] == 0 -> division by zero
    return x

main()