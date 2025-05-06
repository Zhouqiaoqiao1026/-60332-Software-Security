def main():
    x: int = 10
    x = "hello"  # type conflict: str assigned to int
    y: int = x + 1
    return y

main()