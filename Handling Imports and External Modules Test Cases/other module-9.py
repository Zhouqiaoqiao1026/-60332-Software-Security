#Import a specific function from a custom external module.

#other.py
class MyClass:
 pass

def sum(a:int, b:int) -> int:
 return a+b

def sub(a:int, b:int) -> int:
 return a-b


#main 
from other import sum,sub

assert sum(1,2) == 3

a = 2
b = 1
x = sub(a,b)

assert x == 1