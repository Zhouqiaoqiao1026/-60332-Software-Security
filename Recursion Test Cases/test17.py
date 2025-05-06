
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main() -> None:
    assert factorial(3) == 6
main()
