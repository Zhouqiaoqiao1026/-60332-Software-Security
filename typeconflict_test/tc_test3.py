class Person:
    age: int

def main():
    p = Person()
    p.age = "twenty"  # type conflict: str assigned to int
    return p.age

main()