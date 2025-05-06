#type mismatch when calling a function defined in an imported module

[case testErrorInPassTwo1]
import b
[file a.py]
import b
def f() -> None:
    a = b.x + 1
    a + ''
[file b.py]
import a
x = 1 + int()