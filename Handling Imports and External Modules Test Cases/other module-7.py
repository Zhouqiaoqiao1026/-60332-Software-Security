#Import all classes and functions from a custom external module

#other.py
class OtherClass:
 def __init__(self) -> None:
 pass

 def foo(self) -> int:
 return 2

def OtherFunction() -> None:
 pass


#main 
from other import *

obj = OtherClass()
assert obj.foo() == 2

OtherFunction()