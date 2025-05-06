def main():
    x: int = 5
    if True:
        x = "oops"  # type conflict inside conditional branch
    return x + 1

main()