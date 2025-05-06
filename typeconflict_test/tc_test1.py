def add(x: int, y: int) -> int:
    return x + y

def main():
    result: int = add("abc", 2)  # type conflict: str passed to int
    return result

main()