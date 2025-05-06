def give_number() -> int:
    return "not a number"  # type conflict: returning str as int

def main():
    x: int = give_number()
    return x

main()