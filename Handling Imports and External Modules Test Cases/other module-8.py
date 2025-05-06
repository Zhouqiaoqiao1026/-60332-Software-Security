#Import a specific function from a custom external module

#other.py
def OtherFunction() -> int:
 return 1

class OtherClass:
 @classmethod
 def foo(cls) -> int:
 return 3

#main 
import other

assert other.OtherFunction() == 1
assert other.OtherClass.foo() == 3