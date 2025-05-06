def main():
    numbers: list[int] = [1, 2, 3]
    numbers[0] = "oops"  # type conflict: str in list[int]
    return numbers[0]

main()