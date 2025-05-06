def test_fail(x: int):
    assert x != 0
    return 10 // x

test_fail(0)
