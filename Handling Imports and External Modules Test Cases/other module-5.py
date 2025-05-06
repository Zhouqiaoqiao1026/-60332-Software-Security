#There are unimported classes when importing a custom external module.

#other.py
class MyClass:
 def __init__(self) -> None:
 pass

 def bar(self) -> int:
 return 2


class OtherClass:
 def __init__(self) -> None:
 pass

 def foo(self) -> int:
 return 2

#main 
from other import OtherClass

obj1 = OtherClass()
obj2 = MyClass() # Class not imported