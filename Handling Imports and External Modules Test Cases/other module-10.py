#The required function defined in the custom external module was not imported.

#other.py
def foo() -> None:
 pass

def bar() -> None:
 pass


#main 
from other import bar

foo() # Invoking a function that hasn't been imported