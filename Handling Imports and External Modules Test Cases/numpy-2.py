#Calling a function from an imported module with mismatched arguments (not enough arguments)

from numpy import add
def main():
 x = add(1)
 return x
main()