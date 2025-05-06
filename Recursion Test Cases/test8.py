def bad_fib(n: int) -> int:
    return bad_fib(n - 1) + bad_fib(n - 2)

def main() -> None:
    assert bad_fib(3) == 2

main()
