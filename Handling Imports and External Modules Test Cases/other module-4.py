#Properly use aliases for imported modules

# my_module.py Custom module
def sum(a:int, b:int) -> int:
 return a+b

#Main program
import my_module as mp

a = 1
b = 2
x = mp.sum(a,b)
assert x == 3