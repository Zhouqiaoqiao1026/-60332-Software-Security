#Calling a function from an imported module with mismatched arguments (too much arguments)

from numpy import multiply

def main():
 x = multiply(2,3,4)
 assert x == 6

main()