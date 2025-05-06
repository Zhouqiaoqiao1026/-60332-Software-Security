def f(n: int) -> int:
    if n < 0:
        return 0
    return f(n + 1)


def main() -> None:
    assert f(1) == 0  # infinite recursion


main()
