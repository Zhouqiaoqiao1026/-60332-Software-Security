#The required function defined in the custom external module was not imported.

#other.py
class OtherClass:
 def __init__(self) -> None:
 pass

 def foo(self) -> int:
 return 3


def sum(a:int, b:int) -> int:
 return a+b

def sub(a:int, b:int) -> int:
 return a-b


#main 
from other import OtherClass, sum

obj = OtherClass()

assert obj.foo() == 3
assert sum(1,2) == 3
sub(3,2) # Invoking a function that hasn't been imported