def square(x: int) -> int:
    return x * x

def main():
    a = "hello"
    y = square(a)  # type conflict: inferred str passed to int
    return y

main()