#Correctly import the defined classes when importing a custom external module.

#other.py
class OtherClass:
 def __init__(self) -> None:
 pass

 def foo(self) -> int:
 return 2


#main 
from other import OtherClass

obj = OtherClass()
assert obj.foo() == 2